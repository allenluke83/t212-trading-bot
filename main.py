from t_212 import Trading212
from trends import TrendAnalyser
from financial_analysis import AnalyseFinance
from helpers import send_whatsapp
import os
import sys

# This changes the direrctory when crontab is running
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():


    # #Initialise trading212 summary
    t212 = Trading212()
    # 1. Get Account Summary (Balance, P/L, etc.)
    summary = t212.get_data()
    if summary:
        print("--- ACCOUNT SUMMARY ---")
        print(f"Total Value: {summary['totalValue']} {summary['currency']}")
        print(f"Cash: {summary['cash']['availableToTrade']} {summary['currency']}")
        print(f"Invested: {summary['investments']['currentValue']} {summary['currency']}")
        print(f"Unrealized P/L: {summary['investments']['unrealizedProfitLoss']} {summary['currency']}")
    

    # Initialise analysis instance
    analysis = AnalyseFinance(base_monthly=200)

    # Calculate average and closing amounts
    investment = analysis.get_prices(ticker_symbol = "VWRP.L")

    # Check any trends
    trends = TrendAnalyser()

    # Send the table to phone
    send_whatsapp(
        "CURRENT TOP TRENDING STOCKS\n"
        + trends.format_top_stocks(threshold=1,
                                   limit=10)
        )


if __name__ == "__main__":
    main()