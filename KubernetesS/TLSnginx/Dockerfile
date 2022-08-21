FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN \
python3 -m pip install -r requirements.txt

COPY . /app

EXPOSE 8080

CMD [ "gunicorn", "--bind","0.0.0.0:8080", "server:app" ]
