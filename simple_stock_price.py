import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf


st.write("""
# Simple Stock Price Application

Shown are the stock **closing price** and **volume** of Google !

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)
print(tickerData)

tickerDf = tickerData.history(period='1d' , start='2010-5-31' , end ='2020-5-31')

print(tickerDf)
st.write('''## Closing Price''')
st.line_chart(tickerDf.Close)
st.write('''## Volume Price''')
st.line_chart(tickerDf.Volume)
