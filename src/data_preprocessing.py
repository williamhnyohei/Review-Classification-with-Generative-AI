import pandas as pd

def preprocess_data(file_path):
    # Carregar os dados de avaliações
    data = pd.read_csv(file_path)
    
    # Exemplo de limpeza de dados: Remover valores nulos
    data = data.dropna(subset=['review_text'])
    
    # Exemplo de pré-processamento: converter texto para minúsculas
    data['cleaned_text'] = data['review_text'].str.lower()
    
    # Realizar mais passos de limpeza, como remoção de stopwords, etc.
    
    return data

if __name__ == "__main__":
    data = preprocess_data('data/raw/reviews.csv')
    data.to_csv('data/processed/cleaned_reviews.csv', index=False)
