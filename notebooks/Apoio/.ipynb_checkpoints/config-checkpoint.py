from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "dados"
PASTA_MODELOS = PASTA_PROJETO / "dados"

# coloque abaixo o caminho para os arquivos de dados de seu projeto
DADOS_ORIGINAIS = PASTA_DADOS / "employee_attrition.csv"
DADOS_TRATADOS = PASTA_DADOS / "employee_attrition.parquet"

# coloque abaixo o caminho para os arquivos de modelos de seu projeto
MODELO_FINAL = PASTA_MODELOS / "logistic_regression_rus.joblib"