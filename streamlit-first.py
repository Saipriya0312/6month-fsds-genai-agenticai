import streamlit as st
st.title("Saipriya AI dev.A great Data scientist")
st.write("Welcome! This app calculate the square of a number")
st.header("Select a number")
number = st.slider("pick a number",0,100,25)
st.subheader("Result")
s_number = number * number
st.write(f"The square of", number, "is",s_number)