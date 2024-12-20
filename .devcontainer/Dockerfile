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

# Expose ports for backend and frontend
EXPOSE 8080 8501

# Set default CMD to sleep (useful for interactive devcontainers)
CMD ["sleep", "infinity"]
