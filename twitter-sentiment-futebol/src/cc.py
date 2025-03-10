import tweepy
import pandas as pd
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar credenciais da API do Twitter
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Autenticação na API v2
twitter_client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Definir os times a serem monitorados
times = ["Flamengo", "Palmeiras", "São Paulo FC", "Corinthians", "Vasco"]

# Parâmetros de busca
query = " OR ".join(times) + " -is:retweet lang:pt"

# Função para coletar tweets
def coletar_tweets(query, max_tweets=100):
    tweets_data = []
    response = twitter_client.search_recent_tweets(query=query, max_results=max_tweets, tweet_fields=["created_at", "public_metrics", "text", "author_id"])

    for tweet in response.data:
        tweets_data.append({
            "time": tweet.created_at,
            "usuario": tweet.author_id,
            "texto": tweet.text,
            "likes": tweet.public_metrics["like_count"],
            "retweets": tweet.public_metrics["retweet_count"]
        })

    return pd.DataFrame(tweets_data)

# Coletar tweets
df_tweets = coletar_tweets(query, max_tweets=100)

# Salvar em CSV
df_tweets.to_csv("data/tweets_futebol.csv", index=False, encoding="utf-8")
print("✅ Tweets coletados e salvos com sucesso!")