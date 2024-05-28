# Base image
FROM python:3.12

# Set the working directory first
WORKDIR /workspaces/terraform/production

# Copy your Django project code
COPY . .

# Copy requirements.txt and install dependencies 
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt

# Set non-root user (optional for better security)
USER vscode

# Optional: Expose ports
EXPOSE 8000

# Start the Django development server (adjust command if needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]