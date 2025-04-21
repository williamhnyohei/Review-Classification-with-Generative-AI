from src.config.nyt_config import CONFIG as nyt_config
from src.config.reviews_config import CONFIG as reviews_config
from src.data_preprocessing import preprocess_data
from src.classifier import classify
from src.evaluation import evaluate_model
import pandas as pd

# Mude aqui conforme o domínio que quer rodar
CONFIG = nyt_config  # ou reviews_config

if __name__ == "__main__":
    print(f"Rodando pipeline para: {CONFIG.name}")
    data = preprocess_data(CONFIG)
    data = classify(data, CONFIG)

    if CONFIG.has_labels:
        evaluate_model(data, CONFIG)
