FROM python:3.11.6

WORKDIR /usr/src/app

COPY deploy/requirements-minimum.txt ./

RUN pip install --no-cache-dir -r requirements-minimum.txt

COPY django/ ./

CMD exec gunicorn sns.wsgi:application --bind 0.0.0.0:8000