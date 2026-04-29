import requests
from dotenv import load_dotenv
import os

# Load variables from .env into the system environment
load_dotenv()

class Trading212:

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")
        self.base_url = "https://live.trading212.com/api/v0"
        self.endpoint = "/equity/account/summary"

    # This function connects to api to get summary
    def get_data(self):
        url = f"{self.base_url}{self.endpoint}"
        response = requests.get(url, auth=(self.api_key, self.api_secret))
        if response.status_code == 200:
            return response.json()
        print(f"Error fetching {self.endpoint}: {response.status_code}")
        return None
    
    def invest_into_pie(self, pie_id, amount):
        """
        Sends a request to the broker to invest a specific amount into a Pie.
        pie_id: The unique ID or name the broker uses for your Pie.
        amount: The £ amount calculated by your SMA logic.
        """
        endpoint = f"/v1/equity/pies/{pie_id}/investment"
        url = f"{self.base_url}{endpoint}"
        
        # The payload is a JSON with an amount
        payload = {
            "amount": float(amount)
        }

        # Using post here as stuff is being uploaded
        response = requests.post(
            url, 
            json=payload, 
            auth=(self.api_key, self.api_secret)
        )

        if response.status_code == 201 or response.status_code == 200:
            print(f"Successfully sent £{amount} to Pie: {pie_id}")
            return True
        else:
            print(f"Failed to invest: {response.status_code} - {response.text}")
            return False
    