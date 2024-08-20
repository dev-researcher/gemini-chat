from typing import Self
import requests 
from config.settings import ENDPOINT, GOOGLE_CLOUD_API_KEY

class VertexAIClient:
    def __init__(self):
        self.endpoint = ENDPOINT
        self.headers = {
            "Authorization" : f"Bearer {GOOGLE_CLOUD_API_KEY}",
            "Content-Type" : "application/json",
        }
    def send_prompt(self, prompt) : data = {"instances" : [{"prompt": prompt}]}
    response = requests.post(self.endpoint, headers=self.headers, json=data)
    return response.json()