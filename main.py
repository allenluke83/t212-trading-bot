from t_212 import Trading212

def main():

    #Initialise 
    t212 = Trading212()
    # 1. Get Account Summary (Balance, P/L, etc.)
    summary = t212.get_data()
    if summary:
        print("--- ACCOUNT SUMMARY ---")
        print(f"Total Value: {summary['totalValue']} {summary['currency']}")
        print(f"Cash: {summary['cash']['availableToTrade']} {summary['currency']}")
        print(f"Invested: {summary['investments']['currentValue']} {summary['currency']}")
        print(f"Unrealized P/L: {summary['investments']['unrealizedProfitLoss']} {summary['currency']}")
    
    print("\n")

if __name__ == "__main__":
    main()