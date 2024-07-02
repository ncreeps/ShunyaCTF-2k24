FROM php:8-apache

EXPOSE 7100

RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"

COPY src/ /var/www/html/
RUN chmod -R 755 /var/www/html
RUN chown root:root /var/www/html

RUN mkdir -p /var/www/html/files/
RUN chown www-data:www-data /var/www/html/files/
RUN chmod 1733 /var/www/html/files/

RUN echo "0CTF{b4dm0s_bh4y_k4_fl4g}" > /badmosi_k4rk3_fl4g_m1lg4y4.txt
