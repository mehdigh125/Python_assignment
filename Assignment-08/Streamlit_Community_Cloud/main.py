import streamlit as st
import pandas as pd
st.sidebar.title("About")
st.sidebar.write("Upload a csv file and view its line chart and bar chart")

uploaded_file = st.file_uploader("Upload a csv file:", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    x_axis = st.selectbox("X-axis", df.columns)
    y= [col for col in df.columns if col != x_axis]
    y_axis = st.selectbox("Y-axis", y)
    st.write("line chart:")
    st.line_chart(df.set_index(x_axis)[y_axis])
    st.write("bar chart:")
    st.bar_chart(df.set_index(x_axis)[y_axis])
