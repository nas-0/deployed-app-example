#Setting up Dockerfile
FROM python:3.11-slim
WORKDIR /app

#Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy Application Code
COPY . .

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]