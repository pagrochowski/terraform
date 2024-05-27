# Base image
FROM mcr.microsoft.com/devcontainers/base:jammy

# Set the working directory first
WORKDIR /terraform

# Install system dependencies for Chrome and Python
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends golang-go \
       wget gnupg libgconf-2-4 python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install dependencies 
COPY requirements.txt .  
RUN pip install -r requirements.txt

# Set non-root user (optional for better security)
USER vscode

# Optional: Expose ports
EXPOSE 8000
