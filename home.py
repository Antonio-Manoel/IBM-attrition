#Impotações
import pandas as pd
import streamlit as st

from joblib import load

from notebooks.Apoio.config import DADOS_TRATADOS, MODELO_FINAL

#Carragando dados e modelo
@st.cache_data #Cacheia o resultado, evitando ter que recarregar o arquivo, sempre
def carregar_dados():
    return pd.read_parquet(DADOS_TRATADOS)

@st.cache_resource #Esse cache é específico para objetos pesados (modelos)
def carregar_modelo():
    return load(MODELO_FINAL)

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

#colunas com valores ordenados

#colunas com valores ordenados 
generos = sorted(df["Gender"].unique())
niveis_educacionais = sorted(df["Education"].unique())
area_formacao = sorted(df["EducationField"].unique())
departamentos = sorted(df["Department"].unique())
viagem_negocios = sorted(df["BusinessTravel"].unique())
hora_extra = sorted(df["OverTime"].unique())
satisfacao_trabalho = sorted(df["JobSatisfaction"].unique())
satisfacao_colegas = sorted(df["RelationshipSatisfaction"].unique())
satisfacao_ambiente = sorted(df["EnvironmentSatisfaction"].unique())
vida_trabalho = sorted(df["WorkLifeBalance"].unique())
opcao_acoes = sorted(df["StockOptionLevel"].unique())
envolvimento_trabalho = sorted(df["JobInvolvement"].unique()) 

#colunas que serão em slider
colunas_slider = [
    "DistanceFromHome",
    "MonthlyIncome",
    "NumCompaniesWorked",
    "PercentSalaryHike",
    "TotalWorkingYears",
    "TrainingTimesLastYear",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager",
]

#atribuíndo valores máximos e mínimos para cada coluna que será no slider
colunas_slider_min_max = {
    coluna: {"min_value": df[coluna].min(), "max_value": df[coluna].max()}
    for coluna in colunas_slider
} 

#Colunas que serão ignoradas
colunas_ignoradas = (
    "Age",
    "DailyRate",
    "JobLevel",
    "HourlyRate",
    "MonthlyRate",
    "PerformanceRating",
)

#Atribuíndo mediana para as colunas ignoradas
medianas_colunas_ignoradas = {
    coluna: df[coluna].median() for coluna in colunas_ignoradas
}

#Adicionando o título do site
st.title("Attrition Prediction")

#Criando o 1º container
with st.container(border=True):
    st.write("### Personal information")

    widget_genero = st.radio("Gender", generos)
    widget_nivel_educacional = st.selectbox("Educational Level", niveis_educacionais, format_func = lambda numero: niveis_educacao_texto[numero])
    widget_area_formacao = st.selectbox("Field of Study", area_formacao)
    widget_distancia_casa = st.slider("Distance from the house", **colunas_slider_min_max["DistanceFromHome"])