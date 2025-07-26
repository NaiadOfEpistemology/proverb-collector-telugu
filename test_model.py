from transformers import AutoTokenizer,AutoModelForCausalLM
tok=AutoTokenizer.from_pretrained("model/tinyllama-telugu-model")
mdl=AutoModelForCausalLM.from_pretrained("model/tinyllama-telugu-model")

inp="<s>[INST]Explain this Telugu proverb. తినే నోరు తిట్టకుండా ఉండదు.[/INST]"
ids=tok.encode(inp,return_tensors="pt")
out=mdl.generate(ids,max_new_tokens=100)
ans=tok.decode(out[0],skip_special_tokens=True).split("[/INST]")[-1].strip()
print(ans)
