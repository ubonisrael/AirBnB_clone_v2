# A script that installs a nginx server
# Installs nginx on a server
$server_config = "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    add_header X-Served-By \"${hostname}\";

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
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
"
exec { 'update server':
command => '/usr/bin/sudo /usr/bin/apt-get update'
}

package { 'nginx':
ensure  => installed,
require => Exec['update server']
}

exec { 'create web static dirs':
provider => shell,
command  => 'mkdir -p /data/web_static/shared/ && mkdir -p /data/web_static/releases/test/',
before   => Exec['link current to test dir']
}

file { '/etc/nginx/sites-available/default':
ensure  => file,
content => $server_config,
require => Package['nginx'],
notify  => Exec['restart Nginx']
}

exec { 'link current to test dir':
provider => shell,
command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current && chown -R ubuntu:ubuntu /data/',
before   => File['/etc/nginx/sites-available/default'],
}

file { '/var/www/html/index.nginx-debian.html':
ensure  => present,
content => 'Hello World!'
}

file { '/data/web_static/releases/test/index.html':
ensure  => present,
content => 'Welcome to AirBnB clone'
}

file { '/var/www/html/404.html':
ensure  => present,
content => "Ceci n'est pas une page"
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
