# 📊 Repositório de Projetos de Análise Exploratória de Dados (EDA)

## 📌 Sobre este Repositório

Este repositório centraliza diversos projetos de **Análise Exploratória de Dados (EDA)** organizados por dificuldade e temas variados. Cada projeto explora diferentes técnicas de tratamento, visualização e interpretação de dados.

## 🎯 Estrutura dos Projetos
Cada projeto segue a seguinte estrutura de pastas e arquivos:

```
📂 nome-do-projeto/          # Diretório principal do projeto
├── 📁 data                 # Dados brutos e processados
│   ├── raw/               # Dados originais
│   ├── processed/         # Dados limpos e tratados
├── 📁 notebooks            # Notebooks Jupyter para exploração inicial
│   ├── 01_exploracao.ipynb
│   ├── 02_analise.ipynb
├── 📁 src                  # Scripts para análise e visualização de dados
│   ├── load_data.py       # Carregamento e tratamento dos dados
│   ├── eda.py            # Análise exploratória dos dados
│   ├── visualization.py  # Geração de gráficos e dashboards
├── 📄 requirements.txt      # Lista de dependências
├── 📄 README.md             # Documentação do projeto
```

Cada projeto possui **um README.md próprio** com detalhes específicos sobre os dados, as análises realizadas e os insights gerados.

---

## 📊 Projetos e Níveis de Dificuldade

### 🔹 Nível 1 - Iniciante

#### **1. Análise de Notas de Alunos**
**Objetivo:** Explorar um dataset de notas de alunos, entendendo distribuição, médias, e correlações.
- **Aprendizado:**
  - Manipulação de DataFrames com Pandas.
  - Estatísticas básicas (média, mediana, desvio padrão).
  - Gráficos com Matplotlib e Seaborn.
- **DataFrames principais:** `df_notas`

#### **2. Análise de Vendas de E-commerce**
**Objetivo:** Explorar dados de um e-commerce brasileiro para identificar padrões de vendas e tempo de entrega.
- **Aprendizado:**
  - Tratamento de dados e limpeza.
  - Análise de sazonalidade de vendas.
  - Gráficos interativos com Plotly.
- **DataFrames principais:** `df_vendas`, `df_entregas`

---

### 🔸 Nível 2 - Intermediário

#### **3. Análise de Dados Climáticos**
**Objetivo:** Explorar dados meteorológicos e identificar tendências climáticas.
- **Aprendizado:**
  - Trabalhando com datas e séries temporais.
  - Cálculo de médias móveis e análise de tendências.
  - Mapas de calor para visualizar variações climáticas.
- **DataFrames principais:** `df_clima`

#### **4. Sentimento no Twitter sobre Futebol**
**Objetivo:** Coletar e analisar sentimentos em tweets sobre futebol.
- **Aprendizado:**
  - Coleta de dados via API do Twitter (Tweepy).
  - Processamento de texto com NLTK.
  - Classificação de sentimentos (positivo, negativo, neutro).
- **DataFrames principais:** `df_tweets`

---

### 🔺 Nível 3 - Avançado

#### **5. Análise de Desempenho de Jogadores de Futebol**
**Objetivo:** Explorar estatísticas de jogadores e identificar padrões de desempenho.
- **Aprendizado:**
  - Tratamento de grandes volumes de dados.
  - Análise de distribuição e clustering de jogadores.
  - Dashboards interativos.
- **DataFrames principais:** `df_jogadores`

#### **6. Previsão de Demanda em Supermercados**
**Objetivo:** Analisar histórico de vendas e prever demanda futura.
- **Aprendizado:**
  - Modelagem preditiva com machine learning (Regressão, ARIMA, Prophet).
  - Feature engineering e seleção de variáveis.
  - Métricas de avaliação de modelos.
- **DataFrames principais:** `df_vendas_hist`, `df_previsao`

---

## 🚀 Como Utilizar os Projetos

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/eda-projects.git
   cd eda-projects
   ```
2. **Acesse o diretório do projeto desejado e leia a documentação.**
3. **Crie um ambiente virtual e instale as dependências:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```
4. **Execute as análises nos notebooks ou scripts da pasta `src/`.**

---

## 🤝 Contribuição

Sinta-se à vontade para abrir **issues** e enviar **pull requests** para melhorias e novos projetos! 😊

---

Este repositório está em constante evolução, novos projetos serão adicionados! 🚀

