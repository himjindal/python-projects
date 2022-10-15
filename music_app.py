import streamlit as st
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()

st.title ("Music Recommendation Project")

menu = ["Home","Dataset-Upload Sample Data","Dataset-Upload Test Data"]

choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
  st.subheader("Home")
  
elif choice == "Dataset-Upload Sample Data":
  st.subheader("Dataset-Upload Sample Data")
  data_uploaded_sample = st.file_uploader("Please upload sample csv",type=["csv"])
  if data_uploaded_sample is not None:
    read_data_sample = pd.read_csv(data_uploaded_sample)
    df_sample = pd.DataFrame(read_data_sample)
    df_x = df_sample.drop(columns = ["target"])
    df_y = df_sample["target"]
    
    st.write("X_Sample")
    data_x = st.dataframe(df_x)
    
    st.write("Y_Sample")
    data_y = st.dataframe(df_y)
    
    st.write("Congrats File Uploaded")
    
    
elif choice == "Dataset-Upload Test Data":
  st.subheader("Dataset-Upload Test Data")
  data_uploaded_test = st.file_uploader("Please upload test csv",type=["csv"])
  if data_uploaded_test is not None:
    read_data_test = pd.read_csv(data_uploaded_test)
    
    st.write("X_Test")
    df_test = st.dataframe(read_data_test)
    
    st.write("Congrats File Uploaded")
    
from sklearn import datasets
