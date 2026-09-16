#!/usr/bin/env python3
"""Compare same-round MEPS health and employment outcomes by prescription delay."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
import pyreadstat

FLAGS=[f"BRR{i}" for i in range(1,129)]
def estimate(mask, outcome, weight, brr):
    valid=mask & np.isfinite(weight) & (weight>0) & np.isfinite(outcome)
    w=weight[valid]; y=outcome[valid]; p=float((w*y).sum()/w.sum()); reps=[]
    for f in FLAGS:
        rw=w*2*brr.loc[valid,f].to_numpy(float); reps.append(float((rw*y).sum()/rw.sum()))
    se=float(np.sqrt(np.mean((np.asarray(reps)-p)**2)))
    return {"valid_records":int(valid.sum()),"estimate_percent":100*p,"brr_se_percentage_points":100*se,"ci95_percent":[max(0,100*p-1.96*100*se),min(100,100*p+1.96*100*se)]}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("hc256_file",type=Path); ap.add_argument("brr_file",type=Path); ap.add_argument("--output",type=Path,required=True); args=ap.parse_args()
    cols=["DUPERSID","PANEL","DLAYPM42","RTHLTH53","EMPST53","PERWT24F"]
    hc,_=pyreadstat.read_dta(args.hc256_file,usecols=cols); brr,_=pyreadstat.read_dta(args.brr_file,usecols=["DUPERSID","PANEL",*FLAGS])
    hc["KEY"]=hc["DUPERSID"].astype(str)+"|"+hc["PANEL"].astype(str); brr["KEY"]=brr["DUPERSID"].astype(str)+"|"+brr["PANEL"].round().astype(int).astype(str)
    d=hc.merge(brr[["KEY",*FLAGS]],on="KEY",how="left",validate="one_to_one")
    if d["BRR1"].isna().any(): raise ValueError("missing BRR person link")
    w=d["PERWT24F"].to_numpy(float); delay=d["DLAYPM42"].to_numpy(float); health=d["RTHLTH53"].isin([4,5]).to_numpy(float); employed=(d["EMPST53"]==1).to_numpy(float); output={"format":"us-meps-prescription-delay-outcomes-v1","source_unit":"MEPS 2024 HC-256 person with valid prescription-delay field and same-round perceived health/employment outcomes","variance_method":"standard BRR; replicate weight = BRR flag * 2 * PERWT24F","hc256_records":len(d),"results":{}}
    for group,code in (("delay_yes",1),("delay_no",2)):
        mask=delay==code; output["results"][group]={"poor_or_fair_health":estimate(mask,health,w,d),"employed_at_round_5_or_3":estimate(mask,employed,w,d)}
    output["boundary"]="Same-round delay/outcome comparisons are descriptive and selection-sensitive. They do not establish that prescription delay caused health or employment change, and do not observe the dated medication need, adherence, treatment continuity, recovery, trust, or political action. Person weights are not household weights."
    args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(output,indent=2)+"\n"); print(json.dumps(output,indent=2))
if __name__=="__main__": main()
