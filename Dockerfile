FROM python:3.11.6

WORKDIR /usr/src/app

COPY deploy/requirements-minimum.txt ./

RUN pip install --no-cache-dir -r requirements-minimum.txt

COPY deploy/entrypoint.sh ./
RUN chmod +x ./entrypoint.sh

COPY django/ ./

CMD ["/bin/bash", "-c", "./entrypoint.sh"]
