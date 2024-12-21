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
az acr build -r <CONTAINER_REGISTRY_NAME> --image pyoai:v1 .
```


z provider register -n Microsoft.OperationalInsights --wait
az containerapp env create --name fyiEnv --resource-group rg-mvp-jpeast --location japaneast

az containerapp create --name fyioai --resource-group rg-mvp-jpeast --environment fyiEnv --image fyioai.azurecr.io/pyoai:v1 --target-port 8501 --ingress 'external' --registry-server fyioai.azurecr.io --cpu 0.5 --memory 1.0Gi