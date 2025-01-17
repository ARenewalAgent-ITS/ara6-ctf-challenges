FROM sagemath/sagemath-dev:latest

USER root

RUN apt update && apt install socat -y

USER sage

RUN sage -pip install --no-cache-dir pycryptodome

WORKDIR /app

COPY ./src/* ./

CMD socat TCP-LISTEN:5500,reuseaddr,fork EXEC:"sage -python -u /app/chall.py"
