#!/usr/bin/env python3
"""Estimate reported childcare-related work-time loss by SIPP resource endpoint."""
from __future__ import annotations
import argparse, csv, io, json, zipfile
from pathlib import Path
import numpy as np

KEYS=("SSUID","PNUM","SPANEL","SWAVE","MONTHCODE"); REPS=240; FAY=.5
GROUPS=("below_1x","4x_or_more")
def band(v):
    try: v=float(v)
    except (TypeError,ValueError): return None
    return "below_1x" if v<1 else "4x_or_more" if v>=4 else None
def hours(v):
    try:
        v=float(v); return v if 0<=v<=168 else None
    except (TypeError,ValueError): return None
def valid_num(num,den,reps_num,reps_den,n):
    if not n: return {"valid_record_n":0,"weighted_mean_hours":None,"standard_error_hours":None,"approx_95_ci_hours":None}
    mean=num/den; estimates=np.divide(reps_num,reps_den,out=np.full(REPS,np.nan),where=reps_den!=0)
    se=float(np.sqrt(np.nansum((estimates-mean)**2)/(REPS*FAY**2)))
    return {"valid_record_n":n,"weighted_mean_hours":mean,"standard_error_hours":se,"approx_95_ci_hours":[max(0,mean-1.96*se),mean+1.96*se]}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--primary",type=Path,required=True); ap.add_argument("--replicate-zip",type=Path,required=True); ap.add_argument("--output",type=Path,required=True); args=ap.parse_args()
    rows=0; selected={};
    with args.primary.open(encoding="utf-8",newline="") as f:
        rd=csv.DictReader(f); required=set(KEYS)|{"WPFINWGT","THINCPOV","ETIMELOST","ATIMELOST","EWORKMORE","AWORKMORE","THHLDSTATUS","AHINCPOV"}; missing=sorted(required-set(rd.fieldnames or []))
        if missing: raise ValueError("primary slice missing: "+", ".join(missing))
        for r in rd:
            rows+=1
            try: w=float(r["WPFINWGT"])
            except (TypeError,ValueError): continue
            h=hours(r["ETIMELOST"]); g=band(r["THINCPOV"])
            if w<=0 or not g or r["THHLDSTATUS"] not in {"1","2","3","4"} or r["AHINCPOV"] in {"","0"} or r["EWORKMORE"]!="1" or r["AWORKMORE"] in {"","0"} or r["ATIMELOST"] in {"","0"} or h is None: continue
            key=tuple(r[k] for k in KEYS); selected[key]=(g,w,h)
    num={g:0. for g in GROUPS}; den={g:0. for g in GROUPS}; count={g:0 for g in GROUPS}; rn={g:np.zeros(REPS) for g in GROUPS}; rd={g:np.zeros(REPS) for g in GROUPS}; rep_rows=matched=0
    with zipfile.ZipFile(args.replicate_zip) as z, z.open("rw2025.csv") as raw:
        reader=csv.DictReader(io.TextIOWrapper(raw,encoding="utf-8",newline=""),delimiter="|")
        for r in reader:
            rep_rows+=1; item=selected.get(tuple(r[k.lower()] for k in KEYS))
            if item is None: continue
            matched+=1; g,w,h=item; weights=np.fromiter((float(r[f"repwgt{i}"]) for i in range(1,REPS+1)),dtype=float,count=REPS); num[g]+=w*h; den[g]+=w; count[g]+=1; rn[g]+=weights*h; rd[g]+=weights
    output={"format":"us-sipp-childcare-time-loss-resource-v1","source_unit":"valid SIPP reference-parent person-month with EWORKMORE=1 and numeric ETIMELOST, grouped by THINCPOV endpoint","reference_period":"2024","weight":"WPFINWGT; REPWGT1-REPWGT240","variance_method":"Fay BRR, G=240, perturbation factor 0.5","rows_read":rows,"selected_records":len(selected),"replicate_rows_read":rep_rows,"matched_selected_rows":matched,"results":{g:valid_num(num[g],den[g],rn[g],rd[g],count[g]) for g in GROUPS},"boundary":"ETIMELOST is conditional on EWORKMORE=1 and reports fall-reference-year childcare-related work time lost; it is not a monthly loss, population care burden, or causal effect of resources. Person weights are not household weights."}
    args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(output,indent=2)+"\n",encoding="utf-8"); print(json.dumps({k:output[k] for k in ("rows_read","selected_records","replicate_rows_read","matched_selected_rows")},indent=2)); print(json.dumps(output["results"],indent=2))
if __name__=="__main__": main()
