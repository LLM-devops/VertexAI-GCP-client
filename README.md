# VertexAI-GCP-client
## Client inference for a Vertex AI deployed model (GCP)

You need to get GCP authentification credentials in Json format. To do so, follow steps in: https://developers.google.com/workspace/guides/create-credentials?hl=en

- Once you have downloaded the Json credentials file, save it in a folder `data/`

- You then have to fill config.py with models and gcp related parameters

- To inference a deployed vertex AI using gcp_inference.py defined in this repository:

```python
from gcp_inference import authentificate_GCP, create_instance, predict_custom_trained_model_sample
model_name = "gemma-2b-it"
client = authentificate_GCP(model_name)
prompt = "Define RLHF in LLMs alignment."
instance = create_instance(prompt)
answer = predict_custom_trained_model_sample(model_name, client, instance)
```

