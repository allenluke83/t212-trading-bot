# This script will look at trends to estimate investemnt

import yfinance as yf
import pandas as pd
from helpers import get_sp500

class TrendAnalyser:

    def __init__(self):
        """
        
        """
        self.tickers = list(set(get_sp500() + ["VWRP.L"]))


    # Function to scan the markets
    # This is checked on an hourly basis to see any movement over previous hours

    def scan_markets_hourly(self, threshold=2): # Threshold lower for hourly moves
        print(f"Scanning {len(self.tickers)} stocks (Hourly)...")
        
        data = yf.download(
            self.tickers, 
            period="2d", 
            interval="60m", # Check every 60 mins
            group_by='ticker', 
            threads=True, 
            progress=False
        )

        # Iniialise ticker list 
        trending_hits = []
        for ticker in self.tickers:
            try:
                ticker_data = data[ticker].dropna()
                if len(ticker_data) < 5:
                    continue

                # 'Close' is the most recent hourly price
                current_price = float(ticker_data['Close'].iloc[-1])
                # Compare to the price 4 hours ago
                start_price = float(ticker_data['Close'].iloc[-5] )

                pct_change = ((current_price - start_price) / start_price) * 100

                # Check Volume Spike (Current hour vs Avg of last 4 hours)
                current_vol = float(ticker_data['Volume'].iloc[-1])
                avg_vol = float(ticker_data['Volume'].iloc[-5:-1].mean())

                # if price up > threshold% and Volume is higher than average, add it to the 
                if pct_change >= threshold and current_vol > avg_vol:
                    trending_hits.append({
                        "symbol": ticker,
                        "change": round(pct_change, 2),
                        "price": round(current_price, 2),
                        "vol_surge": round(current_vol / avg_vol, 1)
                    })
            except Exception:
                continue

        return sorted(trending_hits, key=lambda x: x['change'], reverse=True)

    