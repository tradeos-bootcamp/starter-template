FROM python:3.11-alpine

WORKDIR /app

RUN pip install fastapi uvicorn

COPY . .

CMD ["python", "-c", "print('Ready!')"]