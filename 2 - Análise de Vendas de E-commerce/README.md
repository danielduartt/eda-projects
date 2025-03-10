# 📊 Análise de Vendas de E-commerce

## 📌 Descrição do Projeto
Este projeto tem como objetivo analisar os padrões de vendas em um e-commerce brasileiro, utilizando dados do **Brazilian E-commerce Public Dataset (Kaggle)**. Serão exploradas tendências de vendas por categoria, sazonalidade e tempo de entrega por região.

## 📂 Estrutura do Repositório
```
📦 ecommerce-sales-analysis
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

## ✅ Objetivos da Análise
1. **Identificar os produtos mais vendidos por categoria.**
2. **Analisar o impacto da época do ano nas vendas.**
3. **Avaliar o tempo médio de entrega por estado/região.**

## 🛠️ Ferramentas Utilizadas
- **Python**
- **Pandas** para manipulação de dados
- **Matplotlib e Seaborn** para visualização de dados
- **Plotly** para gráficos interativos

## 🚀 Como Executar o Projeto
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/ecommerce-sales-analysis.git
   cd ecommerce-sales-analysis
   ```
2. **Crie um ambiente virtual e instale as dependências:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```
3. **Baixe os dados do Kaggle** e coloque-os na pasta `data/raw/`.
4. **Execute as análises nos notebooks ou rode os scripts na pasta `src/`.**

## 📊 Resultados Esperados
Com essa análise, espera-se gerar insights sobre:
- Produtos mais populares e categorias mais lucrativas.
- Sazonalidade das vendas e possíveis estratégias de precificação.
- Eficiência da logística de entrega em diferentes regiões do Brasil.

## 🤝 Contribuição
Fique à vontade para abrir **issues** e enviar **pull requests** com melhorias! 😊

