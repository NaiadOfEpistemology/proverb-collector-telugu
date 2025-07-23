from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
tok = AutoTokenizer.from_pretrained("model/mistral-telugu-model")
mdl = AutoModelForCausalLM.from_pretrained("model/mistral-telugu-model")
gen = pipeline("text-generation", model=mdl, tokenizer=tok)
def _gen(prompt, max_tokens):
    raw = gen(prompt, max_new_tokens=max_tokens, do_sample=True)[0]["generated_text"]
    return raw.split("[/INST]")[-1].strip()
def explain(x): return _gen(f"<s>[INST]Explain this Telugu proverb: {x}[/INST]", 100)
def summarize(x): return _gen(f"<s>[INST]Summarize this proverb: {x}[/INST]", 50)
def casual_tone(x): return _gen(f"<s>[INST]Rewrite this proverb casually: {x}[/INST]", 60)
def poetic_form(x): return _gen(f"<s>[INST]Make this proverb poetic: {x}[/INST]", 80)
def cultural_view(x, region): return _gen(f"<s>[INST]Explain \"{x}\" in the cultural context of {region}[/INST]", 100)
def similar_from(region): return _gen(f"<s>[INST]Give a similar Telugu proverb from {region}[/INST]", 60)
def get_all(x, region):
    return {
        "Explanation": explain(x),
        "Summary": summarize(x),
        "Youth Tone": casual_tone(x),
        "Poetic Form": poetic_form(x),
        "Regional Insight": cultural_view(x, region),
        "Comparable Proverb": similar_from(region)
    }