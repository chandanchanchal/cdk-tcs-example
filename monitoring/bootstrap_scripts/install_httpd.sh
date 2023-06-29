#!/bin/bash -xe

sudo yum install -y httpd
echo "<html><body><h1>Modern Web App</h1></body></html>" >> /var/www/html/index.html
sudo chkconfig httpd on
sudo service httpd start
