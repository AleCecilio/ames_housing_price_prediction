import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


"""
Módulo responsável pela preparação dos dados.

Aqui são realizadas etapas como remoção de outliers,
tratamento de valores faltantes e organização do dataset.
Os dados processados são salvos em arquivos CSV para uso
posterior na análise exploratória e na modelagem.
"""


# Definindo os caminhos para os dados
RAW_PATH = "data/raw/"
PROCESSED_PATH = "data/processed/"


# Função para carregar os dados
def load_csv(path, filename):
    df = pd.read_csv(path + filename)
    return df


# Função para remover outliers
def remove_outliers(df):
    drop_index = df[(df['Gr Liv Area']>4000) & (df['SalePrice']<400000)].index
    df = df.drop(drop_index)
    return df


# Função para salvar os dados sem outliers
def save_data(df, path, filename):
    df.to_csv(path + filename, index=False)


# Função para lidar com dados ausentes
def handle_missing_data(df):
    df = df.drop('PID', axis=1)

    df = df.dropna(axis=0,subset=['Electrical', 'Garage Cars'])

    # BSMT COLUNAS NUMERICAS --> fillna 0
    bsmt_num_cols = [
        'Bsmt Full Bath',
        'Bsmt Half Bath',
        'Bsmt Unf SF',
        'BsmtFin SF 1',
        'BsmtFin SF 2',
        'Total Bsmt SF'
    ]
    df[bsmt_num_cols] = df[bsmt_num_cols].fillna(0)

    # BSMT COLUNAS STRING --> fillna 'None'
    bsmt_str_cols =  [
        'Bsmt Qual',
        'Bsmt Cond',
        'Bsmt Exposure',
        'BsmtFin Type 1',
        'BsmtFin Type 2'
    ]
    df[bsmt_str_cols] = df[bsmt_str_cols].fillna('None')

    df['Mas Vnr Type'] = df['Mas Vnr Type'].fillna('None')
    df['Mas Vnr Area'] = df['Mas Vnr Area'].fillna(0)

    return df


# Função principal para preparar os dados
def prepare_data():

    df = load_csv(RAW_PATH, "Ames_Housing_Data.csv")
    df = remove_outliers(df)
    save_data(df, PROCESSED_PATH, "Ames_outliers_removed.csv")

    df = load_csv(PROCESSED_PATH, "Ames_outliers_removed.csv")
    df = handle_missing_data(df)
    save_data(df, PROCESSED_PATH, "Ames_NO_missing_data.csv")

    # Continua
    return df