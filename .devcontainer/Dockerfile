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

# Copy application requirements (Python dependencies)
COPY app/requirements.txt /workspace/app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /workspace/app/requirements.txt

# Install additional tools (optional)
RUN pip install pytest black

# Install Terraform
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
RUN apt update && sudo apt install -y terraform

# Install CDKTF
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
RUN source ~/.bashrc
RUN nvm install --lts  # Recommended Node.js version
RUN npm install -g cdktf-cli

# Expose ports for backend and frontend
EXPOSE 8080 8501

# Set default CMD to sleep (useful for interactive devcontainers)
CMD ["sleep", "infinity"]
