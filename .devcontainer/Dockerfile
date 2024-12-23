# Base image for Python development with devcontainer features
FROM mcr.microsoft.com/devcontainers/python:3.9

# Set working directory
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    vim \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy required requirements (Python dependencies)
COPY web/requirements.txt /workspace/web/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /workspace/web/requirements.txt

# Install Terraform
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
RUN apt update && sudo apt install -y terraform

# Install CDKTF
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# Install Azure CLI
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Expose ports for backend and frontend
EXPOSE 8080 8501

# Set default CMD to sleep (useful for interactive devcontainers)
CMD ["sleep", "infinity"]
