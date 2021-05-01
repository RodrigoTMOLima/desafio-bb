FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt