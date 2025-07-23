import json
raw=json.load(open("data/proverbs.json","r",encoding="utf-8"))
out=[{"instruction":"Explain this Telugu proverb.","input":x["proverb"],"output":x["meaning"]+" (Region: "+x["region"]+")"} for x in raw]
json.dump(out,open("training_data.json","w",encoding="utf-8"),indent=2,ensure_ascii=False)