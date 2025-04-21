import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def classify(data, config):
    data['sentiment'] = None

    for idx, row in data.iterrows():
        content = row[config.text_column]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente de análise de sentimentos."},
                {"role": "user", "content": f"{config.openai_prompt}\n\n{content}"}
            ]
        )

        prediction = response['choices'][0]['message']['content'].strip()
        data.at[idx, 'sentiment'] = prediction

    data.to_csv(config.output_path, index=False)
    return data
