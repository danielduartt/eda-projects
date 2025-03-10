# 📊 Análise de Sentimento no Twitter sobre Times de Futebol

Este projeto tem como objetivo analisar o sentimento dos torcedores em relação aos times de futebol brasileiro, utilizando tweets coletados do Twitter. A análise busca identificar padrões de opinião positiva, negativa ou neutra ao longo do tempo e durante eventos importantes (ex: jogos, contratações, títulos, etc.).

---

## 🚀 Tecnologias Utilizadas
- **Python**  
- **Tweepy** (coleta de tweets via API do Twitter)  
- **Pandas** (manipulação e limpeza dos dados)  
- **NLTK** (processamento de linguagem natural - NLP)  
- **VADER / BERT** (classificação de sentimento)  
- **Matplotlib & Seaborn** (visualização de dados)  
- **WordCloud** (nuvens de palavras)
- **Dash ou Streamlit** (dashboard interativo)

---

## 📂 Estrutura do Repositório
```
├── data/               # Dados brutos e processados
├── notebooks/          # Jupyter Notebooks com código de exploração e modelagem
├── src/                # Códigos fonte do projeto
│   ├── collect.py      # Script para coletar tweets usando Tweepy
│   ├── preprocess.py   # Funções para limpeza e tratamento de texto
│   ├── sentiment.py    # Modelos de análise de sentimento
│   ├── dashboard.py    # Dashboard interativo com Dash/Streamlit
├── visualizations/     # Gráficos gerados
├── README.md           # Documentação do projeto
```

---

## 📌 Etapas do Projeto

### 1️⃣ Coleta de Dados
- Uso da API do Twitter para coletar tweets com palavras-chave relacionadas a times de futebol.
- Alternativamente, um dataset público do Kaggle pode ser utilizado.

### 2️⃣ Processamento dos Dados
- Remoção de stopwords, links, menções e caracteres especiais.
- Tokenização e normalização do texto.

### 3️⃣ Análise Exploratória (EDA)
- Frequência de tweets por time.
- Nuvem de palavras mais mencionadas.
- Hashtags mais usadas.

### 4️⃣ Classificação de Sentimento
- Aplicar modelos como **VADER** (baseado em regras) ou **BERT** (modelo de deep learning).
- Classificar os tweets como **positivos, negativos ou neutros**.

### 5️⃣ Visualização dos Resultados
- Gráficos mostrando a evolução do sentimento por time ao longo do tempo.
- Comparativo entre times e impacto de eventos.
- Dashboard interativo.

---

## 📊 Exemplos de Visualizações
✅ Gráfico de sentimento ao longo do tempo.  
✅ Comparativo entre times.  
✅ Wordcloud com palavras mais citadas.  

---

## 📎 Como Reproduzir este Projeto
### 🔹 1. Clonar o repositório:
```bash
git clone https://github.com/seu-usuario/twitter-sentiment-futebol.git
cd twitter-sentiment-futebol
```

### 🔹 2. Criar ambiente virtual e instalar dependências:
```bash
python -m venv venv
source venv/bin/activate  # (Linux/macOS)
venv\Scripts\activate  # (Windows)
pip install -r requirements.txt
```

### 🔹 3. Configurar credenciais do Twitter
- Criar uma conta no [Twitter Developer](https://developer.twitter.com/).
- Gerar chaves da API e salvar em um arquivo `.env` com:
  ```
  CONSUMER_KEY=seu_consumer_key
  CONSUMER_SECRET=seu_consumer_secret
  ACCESS_TOKEN=seu_access_token
  ACCESS_TOKEN_SECRET=seu_access_token_secret
  ```

### 🔹 4. Coletar os tweets
```bash
python src/collect.py
```

### 🔹 5. Rodar o modelo de análise de sentimento
```bash
python src/sentiment.py
```

### 🔹 6. Executar o Dashboard
```bash
python src/dashboard.py
```

---

## 📢 Contribuições
Fique à vontade para abrir **Issues** e enviar **Pull Requests** com melhorias e novas funcionalidades! 🙌

---

## 📜 Licença
Este projeto está sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

🚀 **Desenvolvido por [Daniel Duarte]**

