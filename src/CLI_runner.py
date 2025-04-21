import argparse
import pandas as pd
from src.data_preprocessing import preprocess_data
from src.classifier import classify
from src.evaluation import evaluate_model

from src.config.nyt_config import CONFIG as nyt_config
from src.config.reviews_config import CONFIG as reviews_config

CONFIG_MAP = {
    "nyt": nyt_config,
    "reviews": reviews_config,
}

def main(domain: str):
    if domain not in CONFIG_MAP:
        raise ValueError(f"Domínio '{domain}' inválido. Use: {list(CONFIG_MAP.keys())}")
    
    config = CONFIG_MAP[domain]
    print(f">> Executando pipeline para: {config.name}")

    data = preprocess_data(config)
    data = classify(data, config)

    if config.has_labels:
        evaluate_model(data, config)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pipeline de classificação de sentimento.")
    parser.add_argument("--domain", "-d", type=str, required=True,
                        help="Domínio de entrada (nyt, reviews, etc.)")

    args = parser.parse_args()
    main(args.domain)
