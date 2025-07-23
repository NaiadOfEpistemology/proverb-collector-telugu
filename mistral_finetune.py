from transformers import AutoTokenizer,AutoModelForCausalLM
from peft import get_peft_model,LoraConfig,TaskType
from trl import SFTTrainer,SFTConfig
from datasets import load_dataset
import torch
tok=AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
mdl=AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0",device_map={"": "cpu"},torch_dtype=torch.float32)
conf=LoraConfig(r=8,lora_alpha=16,target_modules=["q_proj","v_proj"],bias="none",lora_dropout=0.05,task_type=TaskType.CAUSAL_LM)
mdl=get_peft_model(mdl,conf)
ds=load_dataset("json",data_files="training_data.json",split="train")
fmt=lambda x:f"<s>[INST]{x['instruction']} {x['input']}[/INST] {x['output']}</s>"
cfg=SFTConfig(output_dir="model/mistral-telugu-model",per_device_train_batch_size=1,gradient_accumulation_steps=2,num_train_epochs=1,save_strategy="steps",save_steps=100,logging_steps=20,optim="adamw_torch",bf16=False)
trainer=SFTTrainer(model=mdl,args=cfg,train_dataset=ds,formatting_func=fmt)
trainer.train()
mdl.save_pretrained("model/mistral-telugu-model")
tok.save_pretrained("model/mistral-telugu-model")