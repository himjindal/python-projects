import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()

st.title ("Music Recommendation Project")

menu = ["Home","Dataset"]

choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
  st.subheader("Home")
elif choice == "Dataset":
  st.subheader("Dataset")
  data_uploaded = st.file_uploader("Please upload csv",type=["csv"])
  if data_uploaded is not none:
    read_data = pd.read_csv(data_uploaded)
    st.dataframe(read_data)
