CONFIG = {
    "name": "nyt_sentiment",
    "source_path": "data/raw/nyt_articles.json",
    "text_column": "headline",
    "output_path": "data/processed/nyt_classified.csv",
    "use_openai": True,
    "openai_prompt": "Classifique o sentimento desta manchete como Positivo, Negativo ou Neutro:",
    "has_labels": False
}
