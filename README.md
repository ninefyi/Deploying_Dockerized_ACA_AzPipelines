# Deploying Dockerized AI App in Azure Container Apps using Azure Pipelines

# Run below command to set up CDKTF
```bash
source ~/.bashrc && nvm install --lts && npm install -g cdktf-cli
cdktf --version
```

# Create ENV files
File: /app/.env
```bash
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_KEY=
AZURE_OPENAI_DEPLOYMENT_NAME=
FLASK_APP_PORT=8080
STREAMLIT_PORT=8501
```