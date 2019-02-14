FROM tiangolo/uvicorn-gunicorn-starlette:python3.7

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY ./src /app

ENV GUNICORN_CMD_ARGS="--keyfile privkey.pem --certfile cert.pem --ca-certs chain.pem"
ENV PORT="443"

