import streamlit as st
import numpy as np
import pandas as pd
st.title("Saipriya's second app created on 17/07")
st.write("This app demonstrates the functionalities of streamlit")
st.sidebar.header("User input features")
user_name = st.sidebar.text_input("What is your name??","Streamlit User")
age = st.sidebar.slider("select your age",0,100,25)
fav_colour = st.sidebar.selectbox("What is your favourite colour??", ['Blue','Green','White','Red','Black'])
st.header("Welcome",user_name)
st.write(f"You are {age} years old and your favorite color is {fav_colour}.")
st.subheader("Here is some random data")
data = pd.DataFrame(
    np.random.randn(10,5),
    columns= ('col %d' % i for i in range(5))
    
)
st.dataframe(data)

if st.checkbox("Show Raw Data"):
    st.subheader("Raw data")
    st.write(data)
    
if st.button("Say Hello?"):
    st.write("Hello There")
    
else:
    st.write("Goodbye")