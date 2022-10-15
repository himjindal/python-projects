import streamlit as st
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()

st.title ("Music Recommendation Project")

menu = ["Home","Dataset"]

choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
  st.subheader("Home")
  """The purpose of this web-app is to predict the output from the test file uploaded, using the sample file provided. This ensures that users can easily use new data and still get insights from data. Please note: In Sample data- please ensure you have column labeled target for the app to identify correct X and Y variables."""
  
  
elif choice == "Dataset":
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
    

  st.subheader("Dataset-Upload Test Data")
  
  data_uploaded_test = st.file_uploader("Please upload test csv",type=["csv"])
  
  if data_uploaded_test is not None:
    read_data_test = pd.read_csv(data_uploaded_test)
    
    st.write("X_Test")
    df_test = st.dataframe(read_data_test)
    
    st.write("Congrats File Uploaded")
    
  if data_uploaded_test is not None:
    if data_uploaded_sample is not None:
      model.fit(data_x, data_y)
      y_pred = model.predict(df_test)
      df_pred = df_test.append(y_pred)
      st.write("Final predicted dataset")
      data_pred = st.dataframe(df_pred)

  else:
    st.write("Waiting for the files")
    
