import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import base64
import seaborn as sns


st.title("NBA Player Stats Explorer")

st.markdown("""
This app performs simple Webscraping of NBA player stats data !
* **Python Libraries : ** base64 , pandas , Streamlit
* **Data Source : **[Basketball-refernce.com](https://www.basketball-reference.com/).
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year' , list(reversed(range(1950,2021))))

# Web scraping of NBA player stats

@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url , header = 0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    player_stats = raw.drop(['Rk'] , axis = 'columns')
    return player_stats

player_stats = load_data(selected_year)
print(player_stats)

### Sidebar - Team Selection

sorted_unique_team = sorted(player_stats.Tm.unique())

### Button_sidebar_team

button_team_selection = st.sidebar.button('Allow All Teams')
selected_team = st.sidebar.multiselect('Team',sorted_unique_team,sorted_unique_team)

### Sidebar - Position Selection

sorted_unique_position = sorted(player_stats.Pos.unique())
selected_position = st.sidebar.multiselect('Position' , sorted_unique_position , sorted_unique_position)

### Filtering Data

df_selected_team = player_stats[(player_stats.Tm.isin(selected_team)) & (player_stats.Pos.isin(selected_position))]

##Showing data
st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension :' +str(df_selected_team.shape[0]) + 'Rows and' + str(df_selected_team.shape[1]) + 'Columns')
st.dataframe(df_selected_team)

### Downlaod NBA _data

def file_download(df):
    data = df.to_csv(index=False)
    b64 = base64.b64encode(data.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(file_download(df_selected_team), unsafe_allow_html=True)

# Heatmap
if st.button('Intercorrelation Heatmap'):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.header('Intercorrelation Matrix Heatmap')
    df_selected_team.to_csv('output.csv',index=False)
    df = pd.read_csv('output.csv')
    plt.figure(figsize=(12,7))
    sns.heatmap(df.corr())
    st.pyplot()