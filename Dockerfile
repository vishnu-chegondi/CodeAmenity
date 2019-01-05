# escape = `

FROM ubuntu:16.04

# Install apache2

RUN apt-get -y update

RUN apt-get install -y apache2

RUN apt-get install -y libapache2-mod-wsgi

RUN a2enmod wsgi

# Install python libraries

RUN apt-get install -y python-pip

ADD requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Add the app to the folder

ADD ./Blog /var/www/Blog/

ADD ./blog.wsgi /var/www/

ADD ./Blog.conf /etc/apache2/sites-available/

# Running apache

RUN a2dissite 000-default.conf

RUN a2ensite Blog.conf

EXPOSE 80

CMD apachectl -D FOREGROUND