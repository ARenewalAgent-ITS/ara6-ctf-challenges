FROM php:7.4.33-cli

ENV FLAG1="Part 1 is A"
ENV FLAG2="Part 2 is R"
ENV FLAG3="Part 3 is A"
ENV FLAG4="Part 4 is 6"
ENV FLAG5="Part 5 is {"
ENV FLAG6="Part 6 is g"
ENV FLAG7="Part 7 is a"
ENV FLAG8="Part 8 is a"
ENV FLAG9="Part 9 is d"
ENV FLAG10="Part 10 is a"
ENV FLAG11="Part 11 is _"
ENV FLAG12="Part 12 is i"
ENV FLAG13="Part 13 is d"
ENV FLAG14="Part 14 is e"
ENV FLAG15="Part 15 is _"
ENV FLAG16="Part 16 is b"
ENV FLAG17="Part 17 is i"
ENV FLAG18="Part 18 is k"
ENV FLAG19="Part 19 is i"
ENV FLAG20="Part 20 is n"
ENV FLAG21="Part 21 is _"
ENV FLAG22="Part 22 is s"
ENV FLAG23="Part 23 is o"
ENV FLAG24="Part 24 is a"
ENV FLAG25="Part 25 is l"
ENV FLAG26="Part 26 is _"
ENV FLAG27="Part 27 is e"
ENV FLAG28="Part 28 is w"
ENV FLAG29="Part 29 is k"
ENV FLAG30="Part 30 is w"
ENV FLAG31="Part 31 is k"
ENV FLAG32="Part 32 is e"
ENV FLAG33="Part 33 is }"

WORKDIR /var/www/html

COPY a.php /var/www/html

RUN echo "allow_url_include=On" >> /usr/local/etc/php/conf.d/docker-php.ini

EXPOSE 8080

CMD ["php", "-S", "0.0.0.0:8080"]