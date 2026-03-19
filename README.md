<div align="center">

<br/>

# 🏠 Ames Housing Price Prediction

### Previsão de Preços de Imóveis com Machine Learning

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

![Status](https://img.shields.io/badge/status-concluído-blue?style=for-the-badge)
![Tipo](https://img.shields.io/badge/tipo-portfólio-blueviolet?style=for-the-badge)
![Licença](https://img.shields.io/badge/licença-MIT-green?style=for-the-badge)

</div>

---

## 📌 Sobre o Projeto

Este projeto tem como objetivo **prever o preço de imóveis** utilizando o famoso dataset **Ames Housing**, aplicando técnicas de análise exploratória, engenharia de features e machine learning.

O foco principal é construir um **pipeline completo e modular** — desde o tratamento dos dados brutos até o treinamento, avaliação e salvamento do modelo final. Desenvolvido como projeto de aprendizado e portfólio.

---

## 🎯 Objetivos

| Etapa | Descrição | Status |
|-------|-----------|--------|
| 📊 EDA | Analisar e entender os dados | ✅ |
| 🧹 Limpeza | Tratar valores ausentes e inconsistentes | ✅ |
| ⚙️ Features | Criar novas variáveis relevantes | ✅ |
| 🤖 Modelagem | Treinar modelo de regressão | ✅ |
| 📈 Avaliação | Medir desempenho com métricas | ✅ |
| 💾 Deploy | Salvar o modelo final | ✅ |

---

## 🗂️ Estrutura do Projeto

```
ames-housing/
│
├── 📁 data/
│   ├── raw/                    # Dados originais sem modificação
│   └── processed/              # Dados tratados e prontos para uso
│
├── 📓 notebooks/
│   ├── 01_eda.ipynb            # Análise Exploratória
│   ├── 02_preprocessing.ipynb  # Pré-processamento
│   └── 03_modeling.ipynb       # Modelagem e avaliação
│
├── 🐍 src/
│   ├── data_preprocessing.py   # Tratamento de dados
│   ├── feature_engineering.py  # Engenharia de features
│   ├── train_model.py          # Treinamento do modelo
│   └── data_io.py              # I/O de dados e modelos
│
├── 💾 models/                  # Modelos treinados salvos
├── 🚀 main.py                  # Pipeline principal
├── 📋 requirements.txt
└── 📄 README.md
```

---

## 🗃️ Dataset

O **Ames Housing Dataset** é um dos datasets mais completos para problemas de regressão, contendo mais de 80 variáveis descritivas sobre imóveis residenciais em Ames, Iowa (EUA).

<details>
<summary><strong>📋 Variáveis incluídas (clique para expandir)</strong></summary>

<br/>

- 🏗️ Área do terreno e área construída
- 🌟 Qualidade geral da construção e acabamento
- 📅 Ano de construção e última reforma
- 🛏️ Número de quartos, banheiros e andares
- 🚗 Garagem (tipo, capacidade e condição)
- 🏊 Piscina, varanda e outros extras
- 📍 Vizinhança e zoneamento

</details>

---

## 🛠️ Tecnologias Utilizadas

<div align="center">

| Tecnologia | Uso |
|------------|-----|
| **Python 3.10+** | Linguagem principal |
| **Pandas** | Manipulação e análise de dados |
| **NumPy** | Operações numéricas |
| **Scikit-learn** | Modelagem e avaliação |
| **Joblib** | Serialização do modelo |
| **Jupyter Notebook** | Exploração e prototipagem |

</div>

---

## 📓 Notebooks

### `01_eda.ipynb` — Análise Exploratória
> Entendendo o dataset antes de qualquer transformação.

- Visualização das distribuições de variáveis
- Identificação e análise de valores nulos
- Distribuição e outliers no preço (`SalePrice`)
- Mapa de correlações entre variáveis

### `02_preprocessing.ipynb` — Pré-processamento
> Preparando os dados para o modelo.

- Preenchimento inteligente de valores nulos
- Conversão e padronização de variáveis categóricas
- Remoção de outliers (quando aplicável)

### `03_modeling.ipynb` — Modelagem
> Onde a mágica acontece.

- Testes com diferentes algoritmos de regressão
- Comparação de desempenho por métricas
- Seleção e ajuste do modelo final

---

## 🔩 Módulos (`src/`)

```python
# data_preprocessing.py
# → Tratamento de nulos, padronização de colunas, preparação inicial

# feature_engineering.py
# → Criação de novas features, encoding categórico, seleção de variáveis

# train_model.py
# → Split treino/teste, Lasso Regression, avaliação com RMSE e R²

# data_io.py
# → Carregamento de dados, salvamento do modelo com joblib
```

---

## 🚀 Pipeline Principal

O arquivo `main.py` executa todo o fluxo de forma sequencial e modular:

```python
from src.data_io import load_data, save_model
from src.data_preprocessing import preprocess_data
from src.feature_engineering import create_features
from src.train_model import train_model

# Pipeline completo
data  = load_data()
data  = preprocess_data(data)
data  = create_features(data)
model = train_model(data)
save_model(model)
```

```
📥 Carregar dados
     ↓
🧹 Pré-processamento
     ↓
⚙️  Feature Engineering
     ↓
🤖 Treinamento (Lasso Regression)
     ↓
💾 Salvar modelo → models/
```

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/AleCecilio/ames_housing_price_prediction.git
cd ames_housing_price_prediction
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o pipeline

```bash
python main.py
```

> O modelo treinado será salvo automaticamente em `models/`.

---

## 🔮 Próximos Passos

### Features
- [ ] 🔍 Aplicar **seleção de features** com `SelectFromModel` ou `RFE`
- [ ] 🔄 Testar transformação logarítmica em `SalePrice` para reduzir skewness
- [ ] 🧪 Investigar **interações entre variáveis** (ex: `QualidadeGeral × AreaTotal`)

---

## 👤 Autor

<div align="center">

**Alessandro Moreira Cecilio**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AleCecilio)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/alessandro-cecilio)

*Projeto desenvolvido para aprendizado e portfólio em Ciência de Dados.*

</div>

---

<div align="center">
  <sub>Feito com 🤍 e muito Python</sub>
</div>
