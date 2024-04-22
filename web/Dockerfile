FROM python:latest
ADD . /app
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
COPY index.html .
COPY . .

CMD ["python", "/app/main.py"]