#!/usr/bin/env python3
"""Compare MEPS prescription affordability-delay reports by recorded purchase status."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd
import pyreadstat

FLAGS=[f"BRR{i}" for i in range(1,129)]
GROUPS=("recorded_purchase","no_recorded_purchase")
FIELDS=("DLAYPM42","AFRDPM42")
def share(values, weights, flags, valid, yes):
    w=weights[valid]; y=(values[valid]==yes).to_numpy(); den=w.sum(); point=float((w*y).sum()/den)
    reps=[]
    for f in FLAGS:
        rw=w*2*flags.loc[valid,f].to_numpy(float); reps.append(float((rw*y).sum()/rw.sum()))
    se=float(np.sqrt(np.mean((np.asarray(reps)-point)**2)))
    return {"valid_records":int(valid.sum()),"estimate_percent":100*point,"brr_standard_error_percentage_points":100*se,"ci95_percent":[max(0,100*point-1.96*100*se),min(100,100*point+1.96*100*se)]}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("rx_file",type=Path); ap.add_argument("hc256_file",type=Path); ap.add_argument("brr_file",type=Path); ap.add_argument("--output",type=Path,required=True); args=ap.parse_args()
    rx,_=pyreadstat.read_dta(args.rx_file,usecols=["DUPERSID","PANEL"]); hc,_=pyreadstat.read_dta(args.hc256_file,usecols=["DUPERSID","PANEL","PERWT24F",*FIELDS]); brr,_=pyreadstat.read_dta(args.brr_file,usecols=["DUPERSID","PANEL",*FLAGS])
    rx["KEY"]=rx["DUPERSID"].astype(str)+"|"+rx["PANEL"].astype(str)
    hc["KEY"]=hc["DUPERSID"].astype(str)+"|"+hc["PANEL"].astype(str)
    brr["KEY"]=brr["DUPERSID"].astype(str)+"|"+brr["PANEL"].round().astype(int).astype(str)
    purchaser=set(rx["KEY"]); hc["purchase_status"]=hc["KEY"].map(lambda k:"recorded_purchase" if k in purchaser else "no_recorded_purchase")
    merged=hc.merge(brr[["KEY",*FLAGS]],on="KEY",how="left",validate="one_to_one")
    if merged["BRR1"].isna().any(): raise ValueError("missing BRR person link")
    weights=merged["PERWT24F"].to_numpy(float); output={"format":"us-meps-prescription-purchase-delay-v1","source_unit":"MEPS 2024 HC-256 person, grouped by whether a matching HC-254A prescription event is recorded","variance_method":"standard BRR; replicate weight = BRR flag * 2 * PERWT24F","hc256_records":len(hc),"hc254a_unique_person_panel_keys":len(purchaser),"results":{}}
    for group in GROUPS:
        mask=(merged["purchase_status"]==group).to_numpy() & np.isfinite(weights) & (weights>0)
        output["results"][group]={field:share(merged[field].astype(str),weights,merged,mask,"1") for field in FIELDS}
    output["boundary"]="Recorded prescription purchase is an observed event-selection indicator, not medication need or adherence. People without a recorded HC-254A event may have no prescription, a non-observed/forgone purchase, or another measurement boundary. Delay fields are person-level reported annual measures; no causal purchase or recovery interpretation is made."
    args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(output,indent=2)+"\n"); print(json.dumps(output,indent=2))
if __name__=="__main__": main()
