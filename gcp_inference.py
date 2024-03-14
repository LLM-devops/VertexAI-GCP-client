from google.protobuf.struct_pb2 import Value
from google.protobuf import json_format
from google.oauth2 import service_account
from google.cloud import aiplatform
from typing import Dict, List, Union
import config

def authentificate_GCP(model: str):
    # Create a credentials object using your service account key file
    credentials = service_account.Credentials.from_service_account_file(
        config.GCP_KEY_PATH,
        scopes=['https://www.googleapis.com/auth/cloud-platform']
    )
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": config.API_ENDPOINT(model)}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PredictionServiceClient(credentials=credentials, client_options=client_options)
    return client

def predict_custom_trained_model_sample(
    model: str,
    client,
    instances: Union[Dict, List[Dict]]
):
    """
    `instances` can be either single instance of type dict or a list
    of instances.
    """
    # The format of each instance should conform to the deployed model's prediction input schema.
    instances0 = instances if isinstance(instances, list) else [instances]
    instances = [
        json_format.ParseDict(instance_dict, Value()) for instance_dict in instances0
    ]
    endpoint = client.endpoint_path(
        project=config.PROJECT_ID, location=config.LOCATIONS[model], endpoint=config.ENDPOINTS[model]
    )
    # Prediction
    response = client.predict(
        endpoint=endpoint, instances=instances
    )
    # The predictions are a google.protobuf.Value representation of the model's predictions.
    predictions = response.predictions[-1].split('Output:\n')[1]
    return predictions

def create_instance(prompt: str, max_tokens = config.MAX_TOKENS):
    return {'prompt': prompt,
            'max_tokens': max_tokens}