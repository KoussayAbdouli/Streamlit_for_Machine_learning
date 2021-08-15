import streamlit as st
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import datetime
import requests
import base64
import os
from path import Path


def get_real_time_information(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content , 'html.parser')
    job_elems = soup.find_all('div',class_="maincounter-number")
    d = {}
    d["Coronavirus Cases:"] = job_elems[0].text
    d["Deaths:"] = job_elems[1].text
    d["Recovered:"] = job_elems[2].text
    return d


def get_csv_data(path):
    df = pd.read_csv(path)
    return df

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded