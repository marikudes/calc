FROM python:3.10.12-slim

WORKDIR /app

COPY . /app

RUN pip3 install poetry

RUN poetry install --no-dev

EXPOSE 80

WORKDIR /app/src

CMD ["poetry", "run", "fastapi", "run", "main.py", "--port", "80"]
