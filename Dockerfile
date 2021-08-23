 FROM python:3.8-slim
 WORKDIR /app
 COPY requirements.txt .
 RUN pip install -r requirements.txt
 COPY . .
 CMD gunicorn -k uvicorn.workers.UvicornWorker main:app -b 0.0.0.0:8000


