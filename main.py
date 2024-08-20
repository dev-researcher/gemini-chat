from google.cloud import aiplatform
from config import PROJECT_ID, REGION, MODEL_NAME

def chat_with_model(prompt):
    client = aiplatform.gapic.PredictionServiceClient()
    endpoint = f"projects/{PROJECT_ID}/locations/{REGION}/endpoints/{MODEL_NAME}"
    
    response = client.predict(
        endpoint=endpoint,
        instances=[{"content": prompt}],
        parameters={}
    )
    return response.predictions[0]["content"]

if _name_ == "_main_":
    prompt = input("Say something: ")
    response = chat_with_model(prompt)
    print(f"Model response: {response}")