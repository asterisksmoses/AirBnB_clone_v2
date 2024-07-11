#!/usr/bin/env bash
# A script that sets up your web servers for the deployment of web_static

if ! command -v nginx &> /dev/null; then
	echo "Nginx is not installed. Installing Nginx..."
	sudo apt update
	sudo apt install -y nginx
else
	echo "Nginx already installed."
fi

echo "Creating the directories..."
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "<html>
   <head>
   </head>
   <body>
     Holberton School
   <body>
 </html>" | sudo tee /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]; then
	sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R www-data:www-data /data/

cat << EOF > /etc/nginx/sites-available/default
server {
    listen 80 default_server
    listen [::]:80 default_server;

    root /var/www/html;
    
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}
EOF

sudo systemctl restart nginx

echo "Web static deployment setup complete."
