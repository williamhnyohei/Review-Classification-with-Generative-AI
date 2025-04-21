from .base_config import BaseConfig

CONFIG = BaseConfig(
    name="product_reviews",
    source_path="data/raw/reviews.csv",
    output_path="data/processed/classified_reviews.csv",
    text_column="cleaned_text",
    use_openai=True,
    openai_prompt="Classifique o sentimento desta avaliação de produto:",
    has_labels=True
)
