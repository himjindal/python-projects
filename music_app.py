import streamlit as st

st.title ("Music Recommendation Project")

menu = ["Home","Dataset"]

choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
  st.subheader("Home")
elif choice == "Dataset":
  st.subheader("Dataset")
  data_uploaded = st.file_uploader("Please upload csv",type=["csv"])
