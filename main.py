import requests
import base64
from dotenv import load_dotenv
import os

# Load variables from .env into the system environment
load_dotenv()

# Fetch variables using os.getenv
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BASE_URL = "https://live.trading212.com/api/v0"


def get_data(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, auth=(API_KEY, API_SECRET))
    if response.status_code == 200:
        return response.json()
    print(f"Error fetching {endpoint}: {response.status_code}")
    return None

def main():
    # 1. Get Account Summary (Balance, P/L, etc.)
    summary = get_data("/equity/account/summary")
    if summary:
        print("--- ACCOUNT SUMMARY ---")
        print(f"Total Value: {summary['totalValue']} {summary['currency']}")
        print(f"Cash: {summary['cash']['availableToTrade']} {summary['currency']}")
        print(f"Invested: {summary['investments']['currentValue']} {summary['currency']}")
        print(f"Unrealized P/L: {summary['investments']['unrealizedProfitLoss']} {summary['currency']}")
    
    print("\n")

    # 2. Get Open Positions (Your Investments)
    # positions = get_data("/equity/positions")
    # if positions:
    #     print("--- CURRENT INVESTMENTS ---")
    #     for instrument in positions:
    #         p = instrument['instrument']
    #         #print(f"Ticker: {p['ticker']} | Qty: {p['quantity']} | Current Price: {p['currentPrice']}")

if __name__ == "__main__":
    main()