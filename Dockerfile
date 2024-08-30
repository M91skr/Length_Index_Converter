FROM python:3

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-tk \
    && apt-get clean

COPY . /app

CMD ["python", "main.py"]
