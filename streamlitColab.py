# !pip install -q streamlit
%%writefile app.py
import streamlit as st

st.title("CourseGenApp")
title = st.text_input("Enter your course title", "AAPL")
if st.button("Generate"):
    st.info(title)

# !npm install localtunnel

# !streamlit run app.py &>/content/logs.txt &

# !wget -q -O - ipv4.icanhazip.com

# !npx localtunnel --port 8501