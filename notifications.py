import requests
import urllib.parse

# Your persistent credentials
PHONE = "447931561806"
API_KEY = "4662391"

def send_whatsapp(message):
    """Sends a WhatsApp message via CallMeBot gateway."""
    # Encode the text (converts spaces to %20 so the URL doesn't break)
    encoded_text = urllib.parse.quote(message)
    
    url = f"https://api.callmebot.com/whatsapp.php?phone={PHONE}&text={encoded_text}&apikey={API_KEY}"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("Successfully sent WhatsApp.")
        else:
            print(f"Failed to send. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error connecting to CallMeBot: {e}")