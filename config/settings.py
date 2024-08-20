import os

GOOGLE_CLOUD_PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT_ID")
GOOGLE_CLOUD_API_KEY = os.getenv("GOOGLE_CLOUD_API_KEY")
ENDPOINT = "https://vertex-ai.googleapis.com/v1/projects/smooth-cycling-425323-g1/locations/us-central1/endpoints/{endpoint_id}".format(project_id=GOOGLE_CLOUD_PROJECT_ID, endpoint_id="{endpoint_id}")