import openai
import pandas as pd

# Substitua com sua chave da OpenAI
openai.api_key = 'sua-chave-da-openai'

def classify_reviews(data):
    # Exemplo de uso da OpenAI API para classificar sentimentos
    for index, row in data.iterrows():
        review = row['cleaned_text']
        
        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=f"Classifique o sentimento da seguinte avaliação: {review}",
            max_tokens=50
        )
        
        sentiment = response.choices[0].text.strip()
        data.at[index, 'sentiment'] = sentiment

    return data

if __name__ == "__main__":
    data = pd.read_csv('data/processed/cleaned_reviews.csv')
    data = classify_reviews(data)
    data.to_csv('data/processed/classified_reviews.csv', index=False)
