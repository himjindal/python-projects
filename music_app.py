import streamlit as st

st.title ("Music Recommendation Project")

menu = ['Home','Dataset']

choice = st.sidebar.selections('Menu',menu)

if choice == 'Home':
    st.subheader('Home')
elif choice == 'Dataset':
    st.subheader('Dataset')
