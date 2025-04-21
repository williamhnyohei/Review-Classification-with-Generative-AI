import pandas as pd

def preprocess_data(config):
    data = pd.read_csv(config.source_path) if config.source_path.endswith('.csv') else pd.read_json(config.source_path)

    if config.text_column not in data.columns:
        raise ValueError(f"Coluna '{config.text_column}' não encontrada no dataset.")

    data.dropna(subset=[config.text_column], inplace=True)
    data[config.text_column] = data[config.text_column].str.lower().str.strip()

    return data
