from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://en.wikipedia.org/wiki/2020%E2%80%9321_La_Liga'
CACHE_FILE_NAME1 = 'data/goalscorers.csv'
CACHE_FILE_NAME2 = 'data/assists.csv'


def get_goalscorers():
    try:
        df_goalscorers = pd.read_csv(CACHE_FILE_NAME1)
    except:
        response = requests.request("GET", URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        top_goalscorers = soup.find_all('table', {'class': 'wikitable'})[7]
        df_goalscorers = pd.read_html(str(top_goalscorers))[0]
        df_goalscorers.rename(columns={"Goals[55]": "Goals"}, inplace=True)
        df_goalscorers.to_csv(CACHE_FILE_NAME1, index=False)
    return df_goalscorers


def get_assists():
    try:
        df_assists = pd.read_csv(CACHE_FILE_NAME2)
    except:
        response = requests.request("GET", URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        top_assists = soup.find_all('table', {'class': 'wikitable'})[8]
        df_assists = pd.read_html(str(top_assists))[0]
        df_assists.rename(columns={"Assists[56]": "Assists"}, inplace=True)
        df_assists.to_csv(CACHE_FILE_NAME2, index=False)
    return df_assists
