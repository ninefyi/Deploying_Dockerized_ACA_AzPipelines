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
export GITHUB_SHA=$(git rev-parse HEAD)
export AZ_ACA="fyioai-web"
export AZ_RG="rg-mvp-jpeast"
export AZ_ACR="fyioai"
export AZ_IMG="web"
az acr build -r ${AZ_ACR} --image ${AZ_IMG}:${GITHUB_SHA} .
az containerapp update --name ${AZ_ACA} --resource-group ${AZ_RG}$ --image ${AZ_ACR}$.azurecr.io/${AZ_IMG}:${GITHUB_SHA}
```

```bash
cd api
export GITHUB_SHA=$(git rev-parse HEAD)
export AZ_ACA="fyioai-api"
export AZ_RG="rg-mvp-jpeast"
export AZ_ACR="fyioai"
export AZ_IMG="api"
az acr build -r ${AZ_ACR} --image ${AZ_IMG}:${GITHUB_SHA} .
az containerapp update --name ${AZ_ACA} --resource-group ${AZ_RG}$ --image ${AZ_ACR}$.azurecr.io/${AZ_IMG}:${GITHUB_SHA}
```

```bash
cd api
python app.py 
```

```bash
cd web
streamlit run chat_ui.py --server.port=8501 --server.address=0.0.0.0
```
