FROM ubuntu

RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get install -y python3-pip
RUN apt-get install -y python3
RUN pip3 install --upgrade pip
RUN pip3 install uwsgi supervisor

COPY . /app
RUN pip install -r /app/requirements.txt

WORKDIR /app
RUN mv etc/nginx.conf /etc/nginx/nginx.conf
RUN mv etc/uwsgi.ini /etc/uwsgi.ini
RUN mv etc/supervisord.conf /etc/supervisord.conf


EXPOSE 5000
CMD ["/usr/local/bin/supervisord"]
