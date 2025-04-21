from src.data_preprocessing import preprocess_data
from src.classifier import classify
from src.evaluation import evaluate_model
from src.config.nyt_config import CONFIG as nyt_config
from src.config.reviews_config import CONFIG as review_config

if __name__ == "__main__":
    # Mude isso para "nyt_config" ou "review_config"
    CONFIG = nyt_config

    # 1. Preprocessamento
    data = preprocess_data(CONFIG)

    # 2. Classificação
    classified_data = classify(data, CONFIG)

    # 3. Avaliação (caso tenha rótulos)
    if CONFIG.get("has_labels", False):
        evaluate_model(classified_data, CONFIG)
