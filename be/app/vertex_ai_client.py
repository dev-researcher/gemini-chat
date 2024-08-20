import os
import requests

def send_prompt_to_vertex(prompt):
    api_key = os.getenv("API_KEY")
    project_id = os.getenv("PROJECT_ID")
    endpoint_id = os.getenv("ENDPOINT_ID")
    url = f"https://us-central1-aiplatform.googleapis.com/v1/projects/{project_id}/locations/us-central1/endpoints/{endpoint_id}:predict"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "instances": [{"content": prompt}]
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()