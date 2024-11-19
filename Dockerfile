from python:3.12-slim

env PIP_DISABLE_PIP_VERSION_CHECK=1
env PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN python -m venv venv

RUN pip install -r requirements.txt

COPY ./ /app

EXPOSE 8000

CMD ["python","main.py"]