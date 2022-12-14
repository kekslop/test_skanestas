FROM python:3.8.16-slim

WORKDIR /code

COPY ./src .

RUN pip install -r requirements.txt

CMD ["python3", "-u", "main.py"]
