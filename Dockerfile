FROM python:3.8.16-slim

WORKDIR /code

COPY ./src .

CMD ["python3", "-u", "main.py"]
