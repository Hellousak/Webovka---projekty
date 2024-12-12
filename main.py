import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.JPG")

with col2:
    st.title("Helena S")
    content = """Čus, tohle je moje první webovka"""
    st.info(content)