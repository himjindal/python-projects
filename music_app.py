import streamlit as st

st.title ("Music Recommendation Project")

menu = ["Home","Dataset"]

st.sidebar.selectbox("Menu",menu)
