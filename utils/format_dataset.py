import json

raw=json.load(open("data/proverbs.json","r",encoding="utf-8"))
out=[
  {
    "instruction": "Explain this Telugu proverb.",
    "input": x["proverb"],
    "output": f"{x.get('meaning','(no meaning provided)')} (Region: {x.get('region','Unknown')})"
  }
  for x in raw
]
json.dump(out,open("training_data.json","w",encoding="utf-8"),indent=2,ensure_ascii=False)
print("dataset saved")
