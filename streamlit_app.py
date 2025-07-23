import streamlit as st
import json, os
from utils.generate_response import get_all

st.set_page_config(page_title="Telugu Proverb Collector and Explainer", layout="centered")
st.title("Telugu Proverb Collector and Explainer")
st.caption("Please enter text in Telugu only. Other languages are not supported.")

def save_proverb(proverb, path="data/proverbs.json"):
    data=[]
    if os.path.exists(path):
        try:data=json.load(open(path,"r",encoding="utf-8"))
        except:pass
    data.append({"proverb":proverb})
    with open(path,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)

st.divider()
st.subheader("Submit a New Telugu Idiom")
new_idiom=st.text_input("Enter your idiom (Telugu only)",key="idiom_input")

if st.button("Add Idiom"):
    if new_idiom.strip():
        save_proverb(new_idiom)
        st.success("Idiom saved to proverbs.json")
    else:
        st.error("Please enter a valid idiom in Telugu.")

st.divider()
st.subheader("Interpret a Telugu Proverb")
proverb=st.text_input("Enter a Telugu proverb",key="proverb_input")
region=st.text_input("Optional: Specify a region (e.g., Telangana, Rayalaseema)",key="region_input")

if st.button("Generate Enhanced Responses"):
    if proverb.strip():
        outputs=get_all(proverb,region or "Telugu")
        for label,text in outputs.items():
            st.subheader(label)
            st.write(text)
    else:
        st.error("Please enter a valid Telugu proverb.")