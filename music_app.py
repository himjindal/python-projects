import streamlit as st
import numpy as np
import pandas as pd
import sklearn 
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score
import re
import random
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

import warnings
warnings.filterwarnings('ignore')
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
