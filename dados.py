# Etapa 1: carregar dados #

import pandas as pd

CAMINHO_CSV = "eleicoes.csv"

def dados():
  df = pd.read_csv (CAMINHO_CSV, dtype = {"zona": str, "secao": str})
  return df

if __name__ == "__main__":
    df = dados()
    print(df.head())