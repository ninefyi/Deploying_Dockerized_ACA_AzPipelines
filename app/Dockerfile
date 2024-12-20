# Base image
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080 8501

CMD ["streamlit", "run", "chat_ui.py", "--server.port=8501", "--server.address=0.0.0.0"]
