from .base_config import BaseConfig

CONFIG = BaseConfig(
    name="nyt_sentiment",
    source_path="data/raw/nyt_articles.json",
    output_path="data/processed/nyt_classified.csv",
    text_column="headline",
    use_openai=True,
    openai_prompt="Classifique o sentimento desta manchete como Positivo, Negativo ou Neutro:"
)
