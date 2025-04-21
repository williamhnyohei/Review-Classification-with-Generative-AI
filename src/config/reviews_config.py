CONFIG = {
    "name": "product_reviews",
    "source_path": "data/raw/reviews.csv",
    "text_column": "cleaned_text",
    "output_path": "data/processed/classified_reviews.csv",
    "use_openai": True,
    "openai_prompt": "Classifique o sentimento desta avaliação de produto:",
    "has_labels": True
}
