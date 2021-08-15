import streamlit as st
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import datetime
import requests
import plotly.express as px
import base64
import os
from path import Path

from corona import get_real_time_information,get_csv_data,img_to_bytes


st.set_page_config(layout="wide", page_icon="./images/covid-19.png", page_title="Tunisia Corona Indicator")
st.markdown("<h1 style='text-align:center;'>Tunisia Covid19 Indicator</h1>" , unsafe_allow_html=True)
st.markdown("<br></br>", unsafe_allow_html=True)

d = get_real_time_information("https://www.worldometers.info/coronavirus/country/tunisia/")
print(d)


col1,col2,col3 = st.sidebar.beta_columns(3)
col3.write("")
col2.markdown(
    """
    [<img src='data:image/png;base64,{}' class='center' width=100>](http://www.tunisie.gov.tn/)""".format(
        img_to_bytes("images/gov.png")
    ),

    unsafe_allow_html=True)

col3.write("")
date = st.sidebar.date_input("Today:", datetime.date.today())
st.sidebar.subheader("Improve The Public Trust:")
st.sidebar.subheader("")
st.sidebar.markdown("---")
st.sidebar.subheader("Media Communication:")
com = st.sidebar.selectbox(
    "",
    (   "None",
        "Text",
        "Image",
        "Video"
        )
)
st.sidebar.subheader("Economic Decisions:")
st.sidebar.selectbox(
    "",
    (
        "Fiscalité",
        "Work Hours Reduction"
        "crédit",
    )
)
st.sidebar.subheader("Social Decisions:")
st.sidebar.selectbox(
    "",
    (
        "Grants",
    )
)
st.sidebar.subheader("General Policies:")
st.sidebar.selectbox(
    "",
    (
        "Lockdown",
        "mitigation"
    )
)
st.sidebar.text_area("Commentaire ")

st.markdown("---")
st.subheader("")
st.subheader("")




s = st.beta_columns(3)
s[0].markdown(f"<h1 style='border: 2px solid red'><center>Covid Cases: <br><br>{d['Coronavirus Cases:']}</center></h1>",unsafe_allow_html=True)
s[1].markdown(f"<h1 style='border: 2px solid #808284'><center>Deaths: <br><br>{d['Deaths:']}</center></h1>",unsafe_allow_html=True)
s[2].markdown(f"<h1 style='border: 2px solid green'><center>Recovered: <br><br>{d['Recovered:']}</center></h1>",unsafe_allow_html=True)

#### PLOT CHARTS / DATA
df = get_csv_data('data/covid19.csv')
df_tun = df[df['location'] == 'Tunisia']
df_tun =df_tun.loc[:,['location' , 'date' ,'total_cases']]

if com == 'Text':
    st.markdown("<br></br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;'>Charts Demonstration</h1>" , unsafe_allow_html=True)
    s0,s1 = st.beta_columns(2)

    s0.markdown("<h1>First Plot</h1>" , unsafe_allow_html=True)
    fig = px.line(df_tun, x="date", y="total_cases")
    s0.plotly_chart(fig)
    s1.markdown("<h1>Second Plot</h1>" , unsafe_allow_html=True)
    fig1 = px.scatter(df_tun , x = 'date' , y='total_cases' , title= 'Scatter Plot')
    s1.plotly_chart(fig1)

elif com =='None':
    st.markdown("<br></br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;'>Second Case</h1>" , unsafe_allow_html=True)


