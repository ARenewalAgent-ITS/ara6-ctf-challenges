FROM node:22

WORKDIR /app

COPY ./src .

RUN useradd -ms /bin/bash ctf

RUN chown -R ctf:ctf /app

RUN mv flag.txt /$(cat /dev/urandom | tr -dc 'a-z0-9' | fold -w 8 | head -n 1).txt
RUN chmod 400 /*.txt

USER ctf

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]
