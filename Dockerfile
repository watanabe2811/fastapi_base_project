FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY ./app /app/app
COPY ./requirements.txt /requirements.txt
run pip install -r /requirements.txt