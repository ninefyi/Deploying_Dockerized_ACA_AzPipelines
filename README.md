# Deploying Dockerized AI App in Azure Container Apps using Azure Pipelines

# Create ENV files
File: /app/.env
```bash
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_KEY=
AZURE_OPENAI_DEPLOYMENT_NAME=
FLASK_APP_PORT=8080
STREAMLIT_PORT=8501
```

```bash
az login
```

```bash
az acr login -n <CONTAINER_REGISTRY_NAME> --expose-token
```

```bash
cd web
az acr build -r <CONTAINER_REGISTRY_NAME> --image web:v1 .
```

```bash
cd api
az acr build -r <CONTAINER_REGISTRY_NAME> --image api:v1 .
```
