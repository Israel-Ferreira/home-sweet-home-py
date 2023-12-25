FROM python:3.11-alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 9090

CMD ["python", "/app/hsh_api.py"]

