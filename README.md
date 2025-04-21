# Sentiment Pipeline with OpenAI

This project provides a **modular pipeline** for classifying text data into **sentiments** (positive, negative, neutral) using the **OpenAI API**.  
It is adaptable to multiple domains such as **product reviews**, **news headlines**, or any short text format.

Built with Python, the system supports both **generative AI-based classification** and traditional evaluation via scikit-learn.

---

## 💡 Project Objectives

- Apply Generative AI to classify text data sentiment.  
- Support multiple domains via reusable configurations (`nyt`, `reviews`, etc.).  
- Enable clean modularization: preprocessing → classification → evaluation.  
- Provide a CLI interface for production-ready usage.  

---

## 🚀 Technologies Used

- **Python 3.8+**  
- **OpenAI API** (`gpt-3.5-turbo`)  
- **Pandas** – data manipulation  
- **scikit-learn** – evaluation metrics  
- **dotenv** – API key management  
- **argparse** – CLI interface  
- **Jupyter Notebook** – EDA (optional)  

---

## 📁 Project Structure

```text
project-root/
├── data/
│   ├── raw/               # Unprocessed input data
│   └── processed/         # Cleaned and classified output
│
├── notebooks/             # EDA and insights (optional)
│
├── src/
│   ├── config/            # Modular configuration per domain
│   │   ├── base_config.py
│   │   ├── reviews_config.py
│   │   └── nyt_config.py
│   ├── data_preprocessing.py
│   ├── classifier.py
│   ├── evaluation.py
│   └── cli_runner.py      # Main CLI script
│
├── .env                   # API key (not committed)
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Sentiment-Pipeline-With-OpenAI.git
cd Sentiment-Pipeline-With-OpenAI
```

### 2. Set up environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add your OpenAI API Key
Create a file called `.env` in the root directory:
```dotenv
OPENAI_API_KEY=your-key-here
```

---

## 🧐 Running the Pipeline

```bash
python src/cli_runner.py --domain reviews
```

Available domains:
- `reviews` – product review sentiment analysis
- `nyt` – sentiment classification of NYT headlines

---

## 📦 Input Requirements

### For `reviews`:
- File: `data/raw/reviews.csv`  
- Column required: `cleaned_text`  

### For `nyt`:
- File: `data/raw/nyt_articles.json`  
- Field required: `headline`  

---

## 📊 Output

- Classified data in: `data/processed/<domain>_classified.csv`  
- If `has_labels=True` in config, an evaluation report is printed.

---

## ✨ Coming Soon

- Support for local models (e.g., BERT)  
- Streamlit frontend  
- Logging and metrics dashboard  
- Custom prompt tuning via config  

---

## 📄 License

MIT License © 2025 William Yohei
