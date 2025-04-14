FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y gcc

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
