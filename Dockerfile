# Dockerfile

FROM python:3.11-slim

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

ARG SECRET_KEY
ENV SECRET_KEY=${SECRET_KEY}

RUN apt-get update && apt-get install -y \
    libpq-dev gcc curl && \
    apt-get clean

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
