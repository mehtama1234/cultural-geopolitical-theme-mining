#!/usr/bin/env python3
"""SIPP following-month earnings/hours direction by child-care work prevention."""
from __future__ import annotations
import argparse, csv, io, json, zipfile
from collections import defaultdict
from pathlib import Path
import numpy as np

KEYS=("SSUID","PNUM","SPANEL","SWAVE","MONTHCODE"); REPS=240; FAY=.5
GROUPS=("below_1x","4x_or_more"); CARE=("yes","no"); METRICS=("earnings","hours"); DIRECTIONS=("increase","decrease","same")
def band(v):
    try: v=float(v)
    except (TypeError,ValueError): return None
    return "below_1x" if v<1 else "4x_or_more" if v>=4 else None
def binary(v): return {"1":"yes","2":"no"}.get(v)
def num(v):
    try:
        v=float(v); return v if v>=0 else None
    except (TypeError,ValueError): return None
def direction(a,b): return "increase" if b>a else "decrease" if b<a else "same"
def estimate(cell, nums, dens):
    if not cell["pairs"]: return {"valid_pair_n":0,"share_percent":None,"standard_error_percentage_points":None,"approx_95_ci_percentage_points":None}
    point=100*cell["numerator"]/cell["denominator"]
    ratios=np.divide(nums,dens,out=np.full(REPS,np.nan),where=dens!=0)
    se=float(np.sqrt(np.nansum((ratios-point/100)**2)/(REPS*FAY**2))*100)
    return {"valid_pair_n":cell["pairs"],"share_percent":point,"standard_error_percentage_points":se,"approx_95_ci_percentage_points":[max(0,point-1.96*se),min(100,point+1.96*se)]}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--primary",type=Path,required=True); ap.add_argument("--replicate-zip",type=Path,required=True); ap.add_argument("--output",type=Path,required=True); args=ap.parse_args()
    people=defaultdict(dict); rows=0
    with args.primary.open(encoding="utf-8",newline="") as f:
        rd=csv.DictReader(f); required=set(KEYS)|{"WPFINWGT","THINCPOV","EWORKMORE","AWORKMORE","TPEARN","TMWKHRS"}; missing=sorted(required-set(rd.fieldnames or []))
        if missing: raise ValueError("primary slice missing: "+", ".join(missing))
        for r in rd:
            rows+=1
            try: month,w=int(r["MONTHCODE"]),float(r["WPFINWGT"])
            except (TypeError,ValueError): continue
            if 1<=month<=12 and w>0: people[tuple(r[k] for k in KEYS[:-1])][month]={"resource":r["THINCPOV"],"care":r["EWORKMORE"],"care_flag":r["AWORKMORE"],"earnings":r["TPEARN"],"hours":r["TMWKHRS"],"weight":r["WPFINWGT"]}
    shape=lambda:{d:{"numerator":0.,"denominator":0.,"pairs":0} for d in DIRECTIONS}
    cells={m:{g:{c:shape() for c in CARE} for g in GROUPS} for m in METRICS}; pairs={}
    for person,months in people.items():
        for month in range(1,12):
            cur,nxt=months.get(month),months.get(month+1)
            if not cur or not nxt: continue
            g,c=band(cur["resource"]),binary(cur["care"])
            if not g or not c or cur["care_flag"] not in ("1","2"): continue
            outcomes=[]
            for metric in METRICS:
                a,b=num(cur[metric]),num(nxt[metric])
                if a is None or b is None: continue
                d=direction(a,b); cell=cells[metric][g][c]
                for candidate in DIRECTIONS:
                    cell[candidate]["denominator"]+=float(cur["weight"]); cell[candidate]["numerator"]+=float(cur["weight"])*(candidate==d); cell[candidate]["pairs"]+=1
                outcomes.append((metric,g,c,d))
            if outcomes: pairs[person+(str(month),)]=outcomes
    nums={m:{g:{c:{d:np.zeros(REPS) for d in DIRECTIONS} for c in CARE} for g in GROUPS} for m in METRICS}; dens={m:{g:{c:{d:np.zeros(REPS) for d in DIRECTIONS} for c in CARE} for g in GROUPS} for m in METRICS}
    rep_rows=matched=0
    with zipfile.ZipFile(args.replicate_zip) as z, z.open("rw2025.csv") as raw:
        rd=csv.DictReader(io.TextIOWrapper(raw,encoding="utf-8",newline=""),delimiter="|")
        for r in rd:
            rep_rows+=1; item=pairs.get(tuple(r[k.lower()] for k in KEYS))
            if not item: continue
            matched+=1; weights=np.fromiter((float(r[f"repwgt{i}"]) for i in range(1,REPS+1)),dtype=float,count=REPS)
            for m,g,c,d in item:
                for candidate in DIRECTIONS:
                    dens[m][g][c][candidate]+=weights
                    if candidate==d: nums[m][g][c][candidate]+=weights
    result={"format":"us-sipp-childcare-work-direction-v1","source_unit":"identified person, annual fall child-care work-prevention status at month t to valid earnings/hours direction at month t+1","weight":"WPFINWGT; REPWGT1-REPWGT240","variance_method":"Fay BRR, G=240, perturbation factor 0.5","rows_read":rows,"identified_persons":len(people),"replicate_rows_read":rep_rows,"matched_pair_rows":matched,"cells":{m:{g:{c:{d:estimate(cells[m][g][c][d],nums[m][g][c][d],dens[m][g][c][d]) for d in DIRECTIONS} for c in CARE} for g in GROUPS} for m in METRICS},"boundary":"EWORKMORE is an annual fall reference-parent child-care work-prevention measure, not a dated monthly care event. This is descriptive and does not establish causality, care hours, desired hours, job quality, household prevalence, recovery, trust, political action, or exit."}
    args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps({k:result[k] for k in ("rows_read","identified_persons","replicate_rows_read","matched_pair_rows")},indent=2))
if __name__=="__main__": main()
