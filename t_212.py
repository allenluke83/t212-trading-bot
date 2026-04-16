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

    def get_data(self):
        url = f"{self.base_url}{self.endpoint}"
        response = requests.get(url, auth=(self.api_key, self.api_secret))
        if response.status_code == 200:
            return response.json()
        print(f"Error fetching {self.endpoint}: {response.status_code}")
        return None