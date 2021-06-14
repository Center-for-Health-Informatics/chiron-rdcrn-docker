

# HOW TO GENERATE NEW IMAGE
# 1. create a directory with repositories chiron, chiron_rdcrn, and chiron_rdcrn_docker
# 2. from directory root run the following:
#    docker build -f chiron_rdcrn_docker/dockerfiles/chiron_rdcrn/Dockerfile -t jmeinken/chiron-rdcrn .
#    docker push jmeinken/chiron-rdcrn

FROM python:3.8.5-alpine

RUN pip install --upgrade pip
RUN pip install gunicorn

RUN apk update && apk add python3-dev \
                        gcc \
                        libc-dev \
                        postgresql-dev \
                        musl-dev

COPY ./chiron_rdcrn /app
COPY ./chiron/chiron /app/chiron
COPY ./user_manager /app/user_manager
COPY ./redcap_importer /app/redcap_importer

COPY ./chiron/requirements.txt .
RUN pip install -r requirements.txt
RUN pip install psycopg2

WORKDIR /app

COPY ./chiron_rdcrn_docker/dockerfiles/chiron_rdcrn/entrypoint.sh .
ENTRYPOINT ["sh", "entrypoint.sh"]