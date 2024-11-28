FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY ./requirements.txt /code/requirements.txt

COPY ./src /code/src

COPY .env /code/.env

CMD ["fastapi", "run", "src/main.py", "--port", "80"]






