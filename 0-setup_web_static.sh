#!/usr/bin/env bash
# A script that installs a nginx server
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
printf %s "<html>
  <head>
  </head>
  <body>
    Welcome to AirBnB clone
  </body>
</html>
" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R "$USER":"$USER" /var/www
sudo chown -R "$USER":"$USER" /etc/nginx
echo "Hello World!" > /var/www/html/index.nginx-debian.html
echo "Ceci n'est pas une page" > /var/www/html/404.html
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    add_header X-Served-By "$HOSTNAME";

    location /hbnb_static {
        alias /data/web_static/current/;
        autoindex off;
    }

    location /redirect_me {
        return 301 https://www.goal.com;
    }

    error_page 404 /404.html;
    location = /404.html {
                root /var/www/html;
                internal;
    }
}
" > /etc/nginx/sites-available/default
sudo service nginx restart
