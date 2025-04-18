import requests
from bs4 import BeautifulSoup
import pandas as pd

url = " GET https://api.football-data.org/v4/matches"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Exemplo de extração fictícia de tabela
tabela = soup.find("table", {"id": "resultados"})
df = pd.read_html(str(tabela))[0]

# Exibir as primeiras linhas
print(df.head())
