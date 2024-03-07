#!/usr/bin/env bash
# A script that installs a nginx server
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo chown -R ubuntu:ubuntu /etc/nginx
printf %s "<html>
  <head>
  </head>
  <body>
    Welcome to AirBnB clone
  </body>
</html>
" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;

    # root /var/www/html;
    # index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }

    # location /redirect_me {
    #     return 301 https://www.goal.com;
    # }

    # error_page 404 /404.html;
    # location = /404.html {
    #             root /var/www/html;
    #             internal;
    # }
}
" > /etc/nginx/sites-available/default
sudo service nginx restart
