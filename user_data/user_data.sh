#!/bin/bash
sudo yum update -y
sudo yum -y install httpd php
sudo chkconfig httpd on
sudo service httpd start
sudo echo "<html><body bgcolor="yellow"><h1>hello from chandan</h1></body></html>" >> /var/www/html/index.html