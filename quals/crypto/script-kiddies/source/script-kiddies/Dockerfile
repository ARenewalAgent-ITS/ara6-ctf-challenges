FROM python:latest

RUN apt update
RUN apt install socat -y

WORKDIR /app

RUN pip install pycryptodome

COPY ./src/* ./

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:"python -u ./server.py"
