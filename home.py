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
    st.write("### Personal Information")

    widget_genero = st.radio("Gender", generos)
    widget_nivel_educacional = st.selectbox("Educational Level", niveis_educacionais, format_func = lambda numero: niveis_educacao_texto[numero])
    widget_area_formacao = st.selectbox("Field of Study", area_formacao)
    widget_distancia_casa = st.slider("Distance from the house", **colunas_slider_min_max["DistanceFromHome"])

#Criando o 2º container
with st.container(border=True):
    st.write("### Company Routine")

    #Dividindo o container em 2 colunas
    coluna_esquerda, coluna_direita = st.columns(2)

    with coluna_esquerda:
        widget_departamento = st.selectbox("Department", departamentos)
        widget_viagem_negocios = st.selectbox("Business Travel", viagem_negocios)


    with coluna_direita:
        widget_cargo = st.selectbox("Job Role",
                                    sorted(df[df["Department"] == widget_departamento]["JobRole"].unique())
                                   )
        widget_hora_extra = st.radio("Overtime", hora_extra)

    widget_salario = st.slider("Monthly Income", **colunas_slider_min_max["MonthlyIncome"])

#Criando o 3º container
with st.container(border=True):
    st.write("### Professional Experience")

    #Dividindo o container em 2 colunas
    coluna_esquerda, coluna_direita = st.columns(2)

    with coluna_esquerda:
        widget_empresas_trabalhadas = st.slider("Number Companies Worked", **colunas_slider_min_max["NumCompaniesWorked"])
        widget_anos_trabalhados = st.slider("Total Working Years", **colunas_slider_min_max["TotalWorkingYears"])
        widget_anos_empresa = st.slider("Years At Company", **colunas_slider_min_max["YearsAtCompany"])
        
    with coluna_direita:
        widget_anos_cargo_atual = st.slider("Years In Current Role", **colunas_slider_min_max["YearsInCurrentRole"])
        widget_anos_mesmo_gerente = st.slider("Years With Current Manager", **colunas_slider_min_max["YearsWithCurrManager"])
        widget_anos_ultima_promocao = st.slider("Years Since Last Promotion", **colunas_slider_min_max["YearsSinceLastPromotion"])

#Criando o 4º container
with st.container(border=True):
    st.write("### Satisfaction")

    #Dividindo o container em 2 colunas
    coluna_esquerda, coluna_direita = st.columns(2)

    with coluna_esquerda:
        widget_satisfacao_trabalho = st.selectbox("Job Satisfaction", satisfacao_trabalho, format_func = lambda numero: niveis_satisfacao_texto[numero])
        widget_satisfacao_colegas = st.selectbox("Relationship Satisfaction", satisfacao_colegas, format_func = lambda numero: niveis_satisfacao_texto[numero])
        widget_envolvimento_trabalho = st.selectbox("Job Involvement", envolvimento_trabalho)
    
    with coluna_direita:
        widget_satisfacao_ambiente = st.selectbox("Environment Satisfaction", satisfacao_ambiente, format_func=lambda numero: niveis_satisfacao_texto[numero])
        widget_balanco_vida_trabalho = st.selectbox("Work Life Balance", vida_trabalho, format_func=lambda numero: niveis_vida_trabalho_texto[numero])
        widget_opcao_acoes = st.radio("Stock Option Level", opcao_acoes)

    widget_aumento_salarial = st.slider("Percent Salary Hike (%)", **colunas_slider_min_max["PercentSalaryHike"])
    widget_treinamentos_ultimo_ano = st.slider("Training Times Last Year", **colunas_slider_min_max["TrainingTimesLastYear"])

#Definindo as entradas do modelo
entrada_modelo = {
    "Age": medianas_colunas_ignoradas["Age"],
    "BusinessTravel": widget_viagem_negocios,
    "DailyRate": medianas_colunas_ignoradas["DailyRate"],
    "Department": widget_departamento,
    "DistanceFromHome": widget_distancia_casa,
    "Education": widget_nivel_educacional,
    "EducationField": widget_area_formacao,
    "EnvironmentSatisfaction": widget_satisfacao_ambiente,
    "Gender": widget_genero,
    "HourlyRate": medianas_colunas_ignoradas["HourlyRate"],
    "JobInvolvement": widget_envolvimento_trabalho,
    "JobLevel": medianas_colunas_ignoradas["JobLevel"],
    "JobRole": widget_cargo,
    "JobSatisfaction": widget_satisfacao_trabalho,
    "MaritalStatus": "Single",
    "MonthlyIncome": widget_salario,
    "MonthlyRate": medianas_colunas_ignoradas["MonthlyRate"],
    "NumCompaniesWorked": widget_empresas_trabalhadas,
    "PerformanceRating": medianas_colunas_ignoradas["PerformanceRating"],
    "OverTime": widget_hora_extra,
    "PercentSalaryHike": widget_aumento_salarial,
    "RelationshipSatisfaction": widget_satisfacao_colegas,
    "StockOptionLevel": widget_opcao_acoes,
    "TotalWorkingYears": widget_anos_trabalhados,
    "TrainingTimesLastYear": widget_treinamentos_ultimo_ano,
    "WorkLifeBalance": widget_balanco_vida_trabalho,
    "YearsAtCompany": widget_anos_empresa,
    "YearsInCurrentRole": widget_anos_cargo_atual,
    "YearsSinceLastPromotion": widget_anos_ultima_promocao,
    "YearsWithCurrManager": widget_anos_mesmo_gerente,
}

#Criando um dataframe com as entradas acima
df_entrada = pd.DataFrame([entrada_modelo])

#Criando o botão de previsão
botao_previsao = st.button("Anticipate Attrition")

#Previsão para ser exibido ao clicar no botão
if botao_previsao:
    previsao = modelo.predict(df_entrada)[0]
    probabilidade_atrito = modelo.predict_proba(df_entrada)[0][1]

    cor = ":red" if previsao == 1 else ":green"

    texto_atrito = (f"#### Attrition: {cor}[{"Yes" if previsao == 1 else "No"}]")
    texto_probabilidade = (f"#### Probability of Attrition: {cor}[{probabilidade_atrito:.1%}]")

    st.markdown(texto_atrito)
    st.markdown(texto_probabilidade)