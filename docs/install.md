# Installation Guide for Production Environments

This guide has been used in production with a clean installation of Debian Wheezy.

It currently works with Python 2.7 and contains some hard-coded values:
* `/var/www/trails_challenge` is the root directory of the project
* `trails_challenge` is used a name for every component (users, db, config files)
* the domain is `trailschallenge.ancona5.it`


## System

Install basic packages:

    # apt-get install git postgresql libpq-dev nginx-full python python-pip python-dev screen

Create a Screen session:

    # cd /var/www/trails_challenge
    # screen -S trails_challenge

Add Unix user:

    # adduser trails_challenge

Install Python requirements:

    # pip install -r requirements/base.txt

Clone the project:

    # mkdir -p /var/www && cd /var/www
    # git clone git://github.com/kobe25/trails-challenge

Give the permissions:

    # cd trails_challenge
    # chown -R trails_challenge:trails_challenge .


## Database

Setup role/db on PostgreSQL:

    # sudo -u postgres createuser trails_challenge -P
    # sudo -u postgres createdb trails_challenge -O trails_challenge

Generate the tables and create a superuser:

    # sudo -u trails_challenge python manage.py migrate
    # sudo -u trails_challenge python manage.py createsuperuser

Note: for backup the database:

    # sudo -u postgres pg_dump trails_challenge > ~postgres/trails_challenge_`date -Iminutes`.sql


## Application Server

Start uWSGI (inside the Screen session):

    # uwsgi --ini deploy/uwsgi.ini

Note:  if you need reloading the webserver:

    $ touch /var/www/trails_challenge/deploy/uwsgi.ini


## Web Server

Add to http zone in `/etc/nginx/nginx.conf`:

    http {
      uwsgi_cache_path /tmp/nginx_cache_tc-patrols keys_zone=tc-patrols:10m inactive=1h;
      uwsgi_cache_path /tmp/nginx_cache_tc-techniques keys_zone=tc-techniques:10m inactive=1h;
      uwsgi_cache_path /tmp/nginx_cache_tc-groups keys_zone=tc-groups:10m inactive=1h;
      uwsgi_cache_path /tmp/nginx_cache_tc-tests keys_zone=tc-tests:10m inactive=1h;
      ...
    }

Setup NGiNX:

    # ln -s /var/www/trails_challenge/deploy/nginx /etc/nginx/sites-enabled/trails_challenge
    # nginx -t && service nginx start


## Appendix:  Development

Note:  This section will be reviewed after the dockerization.

BTW, for compiling the client part install `NodeJS`, `NPM` and `coffee` package (`npm install -g coffee`).  Then, build via `Makefile`:

    $ cd /var/www/trails_challenge
    $ make build
