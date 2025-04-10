from sklearn.metrics import classification_report
import pandas as pd

def evaluate_model(data):
    # Supondo que você tenha uma coluna 'sentiment' e uma 'true_sentiment' no seu dataset
    print(classification_report(data['true_sentiment'], data['sentiment']))

if __name__ == "__main__":
    data = pd.read_csv('data/processed/classified_reviews.csv')
    evaluate_model(data)
