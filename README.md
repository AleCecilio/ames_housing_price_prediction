Ames Housing Price Prediction
Sobre o Projeto

Este projeto tem como objetivo prever o preço de imóveis utilizando o dataset Ames Housing, aplicando técnicas de análise de dados e machine learning.

O foco principal é construir um pipeline completo, desde o tratamento dos dados até o treinamento e salvamento do modelo.

Objetivos

Analisar e entender os dados (EDA)

Tratar valores ausentes e inconsistentes

Criar novas variáveis relevantes

Treinar um modelo de regressão

Avaliar o desempenho

Salvar o modelo final

Estrutura do Projeto
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   └── data_io.py
│
├── main.py
├── models/
├── requirements.txt
└── README.md
Dataset

O dataset Ames Housing contém informações detalhadas sobre imóveis, incluindo:

Área do terreno

Qualidade da construção

Ano de construção

Número de quartos

Garagem, piscina, entre outros

Ele é amplamente utilizado em problemas de regressão.

Tecnologias Utilizadas

Python

Pandas

NumPy

Scikit-learn

Joblib

Notebooks
01_eda.ipynb

Responsável pela análise exploratória dos dados:

Visualização das variáveis

Identificação de valores nulos

Distribuição dos preços

Correlação entre variáveis

02_preprocessing.ipynb

Focado no tratamento dos dados:

Preenchimento de valores nulos

Conversão de variáveis categóricas

Remoção de outliers (quando aplicável)

03_modeling.ipynb

Testes de modelos:

Treinamento de diferentes algoritmos

Comparação de desempenho

Escolha do modelo final

Estrutura do Código (src)
data_preprocessing.py

Tratamento de valores ausentes

Padronização de colunas

Preparação inicial dos dados

feature_engineering.py

Criação de novas features

Encoding de variáveis categóricas

Seleção de variáveis relevantes

train_model.py

Divisão treino/teste

Treinamento com Lasso Regression

Avaliação com RMSE e R²

data_io.py

Carregamento de dados

Salvamento do modelo com joblib

Pipeline Principal
main.py

Arquivo responsável por executar todo o fluxo do projeto.

Etapas:

Carregar os dados

Pré-processamento

Feature engineering

Treinamento

Salvamento

Fluxo simplificado:

data = load_data()
data = preprocess_data(data)
data = create_features(data)
model = train_model(data)
save_model(model)
Como Executar
1. Clonar o projeto
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
2. Instalar dependências
pip install -r requirements.txt
3. Executar
python main.py
Modelo Treinado

O modelo final é salvo em:

models/
Possíveis Melhorias

Testar modelos como Random Forest e XGBoost

Aplicar validação cruzada

Criar API (Flask ou FastAPI)

Deploy do modelo

Autor

Alessandro Moreira Cecilio