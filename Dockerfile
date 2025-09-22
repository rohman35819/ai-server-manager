# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Gunakan Python slim
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua kode aplikasi
COPY . .

# Jalankan FastAPI dengan Uvicorn di foreground
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# copy requirements
COPY requirements.txt /app/

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
