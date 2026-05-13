import requests
import urllib.parse
from datetime import datetime
import pytz
import pandas as pd
import requests
from io import StringIO

# YCredentials
PHONE = "447931561806"
API_KEY = "4662391"

def send_whatsapp(message):
    """Sends a WhatsApp message via CallMeBot gateway."""
    # Encode the text (converts spaces to %20 so the URL doesn't break)
    encoded_text = urllib.parse.quote_plus(message)
    
    url = f"https://api.callmebot.com/whatsapp.php?phone={PHONE}&text={encoded_text}&apikey={API_KEY}"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("Successfully sent WhatsApp.")
        else:
            print(f"Failed to send. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error connecting to CallMeBot: {e}")

# Helper function to che k if markets are open
# Checks london and new york whether theyre open

def is_market_open():
    # Get current time in London
    london_tz = pytz.timezone('Europe/London')
    now = datetime.now(london_tz)
    
    #Check for Weekend (5 = Saturday, 6 = Sunday)
    if now.weekday() >= 5:
        return False

    # efine the broad window (London Open to US Close)
    # This covers 08:00 (LSE Open) to 21:00 (NYSE Close) in UK time
    market_start = now.replace(hour=8, minute=0, second=0, microsecond=0)
    market_end = now.replace(hour=21, minute=0, second=0, microsecond=0)

    if market_start <= now <= market_end:
        return True
    
    return False


# This function returns a list of the S&P 500 codes when called 
def get_sp500():

    # Pretend to be a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    # Get S&P 500 from wikipedia
    sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

    # Fetch the page manually first
    response = requests.get(sp500_url, headers=headers)
    sp500_df = pd.read_html(StringIO(response.text))[0]

    return sp500_df['Symbol'].str.replace('.', '-', regex=False).tolist()

