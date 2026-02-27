import streamlit as st
from app import generate_analysis

st.set_page_config(
    page_title="Cricket Analyst Bot",
    layout="centered"
)

st.title("🏏 ICC T20 World Cup Analyst Bot")

query = st.text_input("Ask about teams / standings / qualification:")

if st.button("Analyze"):
    with st.spinner("Generating analysis..."):
        response = generate_analysis(query)
        st.write(response)

st.markdown("---")
st.write("📌 This bot fetches live standings & gives analyst-style answers.")
