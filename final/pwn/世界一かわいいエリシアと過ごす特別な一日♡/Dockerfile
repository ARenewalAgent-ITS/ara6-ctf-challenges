FROM ubuntu:22.04
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get -y install curl \
    build-essential libcunit1-dev libudev-dev socat

RUN useradd ctf
WORKDIR /home/ctf
ADD source/chall /home/ctf/chall
ADD source/flag.txt /home/ctf/flag.txt

RUN chown -R root:root  /home/ctf
RUN chmod -R 555        /home/ctf

RUN mv /home/ctf/flag.txt /home/ctf/flag-$(cat /dev/urandom | tr -dc 'a-f0-9' | fold -w 32 | head -n 1).txt

EXPOSE 1337
ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork,nodelay,su=ctf", "EXEC:'timeout 180 ./chall'"]
