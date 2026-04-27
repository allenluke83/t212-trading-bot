import yfinance as yf
import matplotlib.pyplot as plt

class AnalyseFinance:

    def __init__(self, base_monthly = 100):
        self.base_monthly = base_monthly


    def calculate_sma_investment_logic(self, current_price, sma_200):
        diff_pct = (current_price - sma_200) / sma_200

        # ZONE 1: Business as Usual (Market is doing ok)
        # Price is more than 5% above the average.
        if diff_pct >= 0.05:
            return self.base_monthly

        # ZONE 2: The "Background Top-up" (if market begin to pull back a bit)
        # Price is getting close to the average (between 0% and 5% above).
        # This will trigger more often than other cases
        elif 0 <= diff_pct < 0.05:
            return self.base_monthly * 1.25 # In this reigime return 1.25 times the base amount

        # ZONE 3: The "Value" Zone (Price is slightly below SMA)
        # 0% to 10% below.
        elif -0.10 <= diff_pct < 0:
            return self.base_monthly * 1.5 # Return 1.5 times base amount

        # ZONE 4: The "Fire Sale" (Rare major crash)
        # More than 10% below.
        else:
            return self.base_monthly * 2.0 # Return twice the base amount 
        

    def get_prices(self, ticker_symbol = "VWRP.L"):
        # Download financial data (one year is enough)
        data = yf.download(ticker_symbol, period="1y")

        # Create close price df
        df = data[['Close']].copy()

        # Calculate 200-Day SMA
        df['SMA200'] = df['Close'].rolling(window=200).mean()

        # Extract number required
        current_price = df['Close'].iloc[-1].item()
        sma_200 = df['SMA200'].iloc[-1].item()

        return self.calculate_sma_investment_logic(current_price, sma_200)

# The below function is not used

def simple_plot(ticker="VWRP.L", period="1y"):
    # 1. Download data
    print(f"Downloading data for {ticker}...")
    data = yf.download(ticker, period=period)
    
    if data.empty:
        print("No data found. Check the ticker symbol.")
        return

    # 2. Create the plot
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], label='Closing Price', color='blue')
    
    # 3. Add styling
    plt.title(f"{ticker} - Historical Performance ({period})")
    plt.xlabel("Date")
    plt.ylabel("Price (GBP)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 4. Show it
    print("Generating plot...")
    plt.show()

if __name__ == "__main__":
    simple_plot()