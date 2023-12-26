FROM python:3.11-alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt


EXPOSE 9090


CMD ["gunicorn", "--bind", "0.0.0.0:9090", "hsh_api:app"]

