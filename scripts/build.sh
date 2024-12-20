#!/bin/bash
set -e
docker build -t exampleacr123.azurecr.io/backend:latest -f app/Dockerfile .
docker build -t exampleacr123.azurecr.io/frontend:latest -f app/Dockerfile .
