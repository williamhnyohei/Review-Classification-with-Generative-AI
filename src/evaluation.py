from sklearn.metrics import classification_report

def evaluate_model(data, config):
    if 'true_sentiment' not in data.columns or 'sentiment' not in data.columns:
        raise ValueError("Dataset precisa ter as colunas 'true_sentiment' e 'sentiment' para avaliação.")

    print(f"\nAvaliação para: {config.name}\n")
    print(classification_report(data['true_sentiment'], data['sentiment']))
