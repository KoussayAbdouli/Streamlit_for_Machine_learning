import streamlit as st
import pandas as pd
import numpy as np
import base64
import yfinance as yf
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)


###
st.title('S&P 500 App')

st.markdown("""
This app retrieves the list of the **S&P 500** (from Wikipedia) and its corresponding **stock closing price** (year-to-date)!
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
""")

st.sidebar.header('User Input Features')

###Web Scraping

@st.cache
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url , header=0)
    df = html[0]
    return df

df = load_data()
sector = df.groupby('GICS Sector')


###Sidebar - Sector Selection
sorted_sector_unique = sorted(df['GICS Sector'].unique())
selected_sector = st.sidebar.multiselect('Sectors' ,sorted_sector_unique,sorted_sector_unique )

#Filtering Data
df_selector_sector = df[(df['GICS Sector'].isin(selected_sector))]

st.header('Display Companies in Selected Sector')
st.write('Data Dimension :' +str(df_selector_sector.shape[0]) + 'Rows and' + str(df_selector_sector.shape[1]) + 'Columns')
st.dataframe(df_selector_sector)

### Download the data

def file_download(df):
    data = df.to_csv(index=False)
    b64 = base64.b64encode(data.encode()).decode()
    href = f'<a href="data:data/file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href

st.markdown(file_download(df_selector_sector), unsafe_allow_html=True)




data = yf.download(
    tickers = list(df_selector_sector[:10].Symbol),
    period = "ytd",
    interval = "1d",
    group_by = 'ticker',
    auto_adjust = True,
    prepost = True,
    threads = True,
    proxy = None
)

# Plot Closing Price of Query Symbol
def price_plot(symbol):
    df = pd.DataFrame(data[symbol].Close)
    df['Date'] = df.index
    plt.fill_between(df.Date, df.Close, color='skyblue', alpha=0.3)
    plt.plot(df.Date, df.Close, color='skyblue', alpha=0.8)
    plt.xticks(rotation=90)
    plt.title(symbol, fontweight='bold')
    plt.xlabel('Date', fontweight='bold')
    plt.ylabel('Closing Price', fontweight='bold')
    return st.pyplot()

num_company = st.sidebar.slider('Number of Companies', 1, 5)

if st.button('Show Plots'):
    st.header('Stock Closing Price')
    for i in list(df_selector_sector.Symbol)[:num_company]:
        price_plot(i)
