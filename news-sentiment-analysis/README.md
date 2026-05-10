# Nova Financial Solutions: News Sentiment & Stock Analysis

## 🎯 Business Objective
To enhance predictive analytics for investment teams by correlating financial news sentiment with stock price movements.

## 🚀 Setup Instructions
1. Clone the repo: `git clone <repo-url>`
2. Create Venv: `python -m venv venv`
3. Activate: `source venv/bin/activate` (or `.\venv\Scripts\activate` on Windows)
4. Install: `pip install -r requirements.txt`

## 📊 Data Sources
- **FNSPID**: Financial news headlines and metadata.
- **YFinance**: Historical stock price data (OHLCV).

## 🛠 Usage
- Run EDA: `jupyter notebook notebooks/eda.ipynb`
- Run Indicators: `python src/analysis/indicators.py`
- Run Tests: `pytest`