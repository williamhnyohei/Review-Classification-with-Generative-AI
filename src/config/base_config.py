from dataclasses import dataclass

@dataclass
class BaseConfig:
    name: str
    source_path: str
    output_path: str
    text_column: str
    use_openai: bool
    openai_prompt: str
    has_labels: bool = False
