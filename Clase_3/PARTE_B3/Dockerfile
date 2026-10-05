FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN echo "Este mensaje se ejecutó durante el build"

COPY script.py .

CMD ["python", "script.py"]