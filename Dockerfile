FROM python:3.11.1-slim

# Create app directory
WORKDIR /app

# Install Jupyter
RUN pip install jupyter

# Optional: Install other requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application files
COPY . .

# Ensure permissions
RUN chmod -R 777 /app

# Command to run Jupyter or the necessary scripts
CMD ["jupyter", "nbconvert", "--to", "notebook", "/app/multivate_linear_reg.ipynb"]
