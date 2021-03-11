
FROM python:3.8-alpine
WORKDIR /django
RUN apk update && \
  apk add bash make gcc g++ postgresql-dev jpeg-dev zlib-dev 
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
ENTRYPOINT [ "docker/entrypoint.sh" ]
ENV PYTHONDONTWRITEBYTECODE=1
COPY ./ ./
