#Impotações
import pandas as pd
import streamlit as st

from joblib import load

from notebooks.src.config import DADOS_TRATADOS, MODELO_FINAL

#Carragando dados e modelo
@st.cache_data #Cacheia o resultado, evitando ter que recarregar o arquivo, sempre
def carregar_dados():
    return pd.parquet(DADOS_TRATADOS)

@st.cache_resource #Esse cache é específico para objetos pesados (modelos)
def carregar_modelo():
    return load (MODELO_FINAL)

df = carregar_dados()
modelo = carregar_modelo()

#Adicionando um texto para algumas colunas numéricas, mas que possuem ordem (Consultar o Dicionário de Dados)
niveis_educacao_texto = {
    1:"Below College",
    2:"College",
    3:"Bachelor",
    4:"Master",
    5:"PhD"
}

niveis_satisfacao_texto = {
    1:"Low",
    2:"Medium",
    3:"High",
    4:"Very High"
}

niveis_vida_trabalho_texto = {
    1:"Low",
    2:"Medium",
    3:"High",
    4:"Very High"
}


#RelationshipSatisfaction  | Numerical Value - 1=Low, 2=Medium, 3=High, 4=Very High 
#WorkLifeBalance          | Numerical Value - 1=Bad, 2=Good, 3=Better, 4=Best 



#Colunas que serão ignoradas
colunas_ignoradas = (
    "Age",
    "DailyRate",
    "JobLevel",
    "HourlyRate",
    "MonthlyRate",
    "PerformanceRating",
)

medianas_colunas_ignoradas = {
    coluna: df[coluna].median() for coluna in colunas_ignoradas
}