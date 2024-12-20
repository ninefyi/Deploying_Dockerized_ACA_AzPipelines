#!/bin/bash
set -e
az acr login --name exampleacr123
docker push exampleacr123.azurecr.io/backend:latest
docker push exampleacr123.azurecr.io/frontend:latest
