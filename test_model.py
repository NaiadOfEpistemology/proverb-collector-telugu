from transformers import AutoTokenizer,AutoModelForCausalLM
import torch
tok=AutoTokenizer.from_pretrained("model/mistral-telugu-model")
mdl=AutoModelForCausalLM.from_pretrained("model/mistral-telugu-model")
input="<s>[INST]Explain this Telugu proverb. తినే నోరు తిట్టకుండా ఉండదు.[/INST]"
ids=tok.encode(input,return_tensors="pt")
out=mdl.generate(ids,max_new_tokens=100)
print(tok.decode(out[0]))