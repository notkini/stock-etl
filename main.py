import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# Load your API key
load_dotenv()
API_KEY = os.environ['ALPHAVANTAGE_API_KEY']

# Stock symbol to fetch
symbol = "IBM"

# Alpha Vantage endpoint
URL = "https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": symbol,
    "apikey": API_KEY
}

# GET request
response = requests.get(URL, params=params)
data = response.json()

# Save data to data/ folder
Path("data").mkdir(exist_ok=True)
with open(f"data/{symbol}_daily.json", "w") as f:
    import json
    json.dump(data, f)

print(f"Saved {symbol} data to data/{symbol}_daily.json")
