FROM ubuntu:22.04
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get -y install curl \
    build-essential libcunit1-dev libudev-dev socat

RUN useradd ctf
WORKDIR /home/ctf
ADD release/ .
ADD 'source/mandatory flag checker/flag.txt' /home/ctf/flag.txt

RUN chown -R root:root  /home/ctf
RUN chmod -R 555        /home/ctf

EXPOSE 1337
ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork,nodelay,su=ctf", "EXEC:'timeout 180 ./chall'"]