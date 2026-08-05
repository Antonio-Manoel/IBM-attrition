# Previsão de Attrition de uma empresa

Através de uma base de dados retirada do Kaggle, fiz um projeto dividido em algumas etapas:
- Análise Exploratória de Dados (EDA)
- Machine Learning
- Criação de um app com streamlit

**OBS.: Como a base estava em inglês, optei por fazer o app do streamlit no mesmo idioma**
**OBS.: O app foi feito na versão gratuita do streamlit, então depois de um tempo, ele entra em modo de hibernação e apenas o criador pode reativar**



**Origem dos dados:** https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset/data

**Link do app:** https://ibm-attrition-ytbfz4xg6zcvqfqjkv7dgq.streamlit.app/


## Um pouco sobre a base
Este projeto utiliza o conjunto de dados IBM HR Analytics Employee Attrition & Performance, disponibilizado no Kaggle. 
Trata-se de um conjunto de dados fictício, criado por cientistas de dados da IBM, contendo informações demográficas, profissionais e de satisfação de 1.470 funcionários distribuídas em 35 atributos. 
O principal objetivo é prever a variável Attrition, que indica se um colaborador deixou ou permaneceu na empresa.

## Organização do projeto
- .gitignore         <- Arquivos e diretórios a serem ignorados pelo Git
- requirements.txt       <- O arquivo de requisitos para reproduzir o ambiente de análise
- LICENSE            <- Licença de código aberto (MIT)
- README.md          <- README principal para desenvolvedores que usam este projeto.
- dados              <- Arquivos de dados para o projeto.
- notebooks          <- Jupyter Notebooks.
-Apoio             <- Pasta com arquivos .py usados no projeto
  - auxiliares.py  <- Funções para ajudar na visualização de dados 
  - config.py    <- Configurações básicas do projeto
  - graficos.py  <- Funções para criação de gráficos personalizados
  - modelos.py  <- Funções para criação de modelos usados no projeto      