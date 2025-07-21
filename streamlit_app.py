from datetime import datetime
import json
import os
import streamlit as st
st.set_page_config(page_title="Telugu Proverb Collector", layout="centered")
st.markdown("""
### This AI can understand Telugu (hopefully)
""")
proverb=st.text_input("Enter a Telugu idiom/proverb/quote : ")
meaning=st.text_area("What does this idiom/proverb/quote mean? ")
region=st.selectbox("Choose Region",["TS","AP","Other"])
if st.button("Submit") and proverb and meaning:
    entry={"proverb":proverb, "meaning":meaning, "region":region,"timestamp":datetime.now().isoformat()}
    os.makedirs("data",exist_ok=True)
    path="data/proverbs.json"
    data=[]
    if os.path.exists(path):
        with open(path,"r") as f:
            try:
                data=json.load(f)
            except json.JSONDecodeError:
                data=[]
    data.append(entry) #time now is 10:34 AM 21/07/25
    with open(path,"w") as f:
        json.dump(data,f,indent=2)
    st.success("Saved. Thank you for your contribution.")
st.markdown("## Recent Submissions : ")
path="data/proverbs.json"
if os.path.exists(path):
    with open(path,"r") as f:
        try:
            entries=json.load(f)[-5:]
            for e in reversed(entries):
                st.markdown(f"""
**Proverb** : {e['proverb']}\n
**Meaning** : {e['meaning']}\n
**Region** : {e['region']}\n
**Time** : {e['timestamp']}
---""")
        except json.JSONDecodeError:
            st.warning("No valid submissions yet")
else:
    st.info("No entries available.")

