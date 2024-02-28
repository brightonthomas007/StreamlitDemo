import streamlit as st
import pandas as pd

st.header("Hello World")
ans=st.checkbox("This is a checkbox")

if ans:

    st.write("Ticked")