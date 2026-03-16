import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.data_io import load_processed, save_processed


"""
Módulo responsável pela engenharia de features.

Nesta etapa são transformadas variáveis categóricas em
variáveis numéricas através da criação de dummies,
preparando os dados para os modelos de machine learning.
"""


def create_dummies(df):
    """Converte variáveis categóricas em variáveis dummies."""

    # Separar colunas categóricas e numéricas
    df_object = df.select_dtypes(include='object')
    df_numeric = df.select_dtypes(exclude='object')

    # Criar variáveis dummies
    df_object_dummies = pd.get_dummies(df_object, drop_first=True)

    # Combinar variáveis numéricas com as novas dummies
    df_final = pd.concat([df_numeric, df_object_dummies], axis=1)

    return df_final


def feature_engineering():
    """Pipeline de engenharia de features."""

    # Carregar dataset já tratado (sem valores ausentes)
    df = load_processed("Ames_NO_missing_data.csv")

    # Criar variáveis dummies
    df = create_dummies(df)

    # Salvar dataset final para modelagem
    save_processed(df, "Ames_Final_DF.csv")

    return df