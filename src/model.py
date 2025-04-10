import openai
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

openai.api_key = os.getenv('OPENAI_API_KEY')  # Agora carrega a chave da variável de ambiente

if openai.api_key is None:
    raise ValueError("Chave da API da OpenAI não encontrada no arquivo .env.")

def classify_reviews(data):
    # Exemplo de uso da nova API da OpenAI para classificar sentimentos
    for index, row in data.iterrows():
        review = row['cleaned_text']
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "Você é um assistente especializado em análise de sentimentos."},
                {"role": "user", "content": f"Classifique o sentimento da seguinte avaliação: {review}"}
            ]
        )
        
        sentiment = response['choices'][0]['message']['content'].strip()
        data.at[index, 'sentiment'] = sentiment

    return data

if __name__ == "__main__":
    # Carregar o arquivo de dados
    data = pd.read_csv('data/processed/cleaned_reviews.csv')
    
    # Classificar as avaliações
    data = classify_reviews(data)
    
    # Salvar as avaliações classificadas
    data.to_csv('data/processed/classified_reviews.csv', index=False)
