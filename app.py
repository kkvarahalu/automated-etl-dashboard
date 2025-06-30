import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
st.set_page_config(page_title="ETL+Dashboard",layout="wide")
st.title("Automated ETL+Dashboard System")
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])
if uploaded_file:
    df=pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
    st.subheader("Preview")
    st.dataframe(df.head())
    st.subheader("Handle Missing Values")
    option=st.selectbox("Choose", ["None", "Drop", "Mean", "Median"])
    if option=="Drop":
        df=df.dropna()
    elif option=="Mean":
        df=df.fillna(df.mean(numeric_only=True))
    elif option=="Median":
        df=df.fillna(df.median(numeric_only=True))
    st.subheader("Summary Statistics")
    st.write(df.describe())
    st.subheader("Visualization")
    col=st.selectbox("Select column",df.columns)
    chart=st.selectbox("Chart type",["Box","Histogram","Pie","Scatter"])
    if chart=="Box":
        st.plotly_chart(px.box(df,y=col))
    elif chart == "Histogram":
        st.plotly_chart(px.histogram(df,x=col))
    elif chart=="Pie":
        st.plotly_chart(px.pie(df,names=col))
    elif chart=="Scatter":
        x_col=st.selectbox("Select X-axis",df.columns)
        y_col=st.selectbox("Select Y-axis",df.columns)
        st.plotly_chart(px.scatter(df,x=x_col,y=y_col,color=df.columns[-1]))
    st.subheader("Download Cleaned Data")
    st.download_button("Download CSV", df.to_csv(index=False), "cleaned_data.csv")
