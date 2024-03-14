# LLMs parameters ---------------------------------------------------------------------------------------------------------------------------------------------
MODELS = ['gemma-2b-it', 'mistral-7b-it', 'starcoder-2']
# endpoints
ENDPOINTS = {"gemma-2b-it": "",
             "mistral-7b-it": ""}
# Loacations
LOCATIONS = {"gemma-2b-it": "",
             "mistral-7b-it": ""}

# Default maximum token value
MAX_TOKENS = 700

# GCP parameters --------------------------------------------------------------------------------------------------------------------------------------------
# Cloud IDs
PROJECT_ID= ""
GCP_KEY_PATH = 'data/gcp-auth-key.json'
API_ENDPOINT: str = lambda model_name: f"{LOCATIONS[model_name]}-aiplatform.googleapis.com"


