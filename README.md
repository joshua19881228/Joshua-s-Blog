# Joshua-s-Blog

I start up this repo to manage the code of my personal website [Joshua's Blog](http://joshua881228.webfactional.com), which is set up on [WebFaction](https://www.webfaction.com/) and implemented by [Django](https://www.djangoproject.com/) and several other packages.

In addition to manage my own code, viewers can also use this project to learn how to build a website using Django. I will write down the works that need to be done to use these code.

Finally, welcome to visit [Joshua's Blog](http://joshua881228.webfactional.com).

## Environment

1. [Ubuntu 14.04](http://www.ubuntu.com/). Though Ubuntu 16.04 has been released for a while, I am still using an older LTS release. I am not sure the following instruction can work fine on Ubuntu 16.04.
2. [Apache 2.4](http://httpd.apache.org/). I chose Apache 2.4 because my deploy server is powered by Apache 2.4. The Apache HTTP Server Project is an effort to develop and maintain an open-source HTTP server for modern operating systems including UNIX and Windows. 
3. [WSGI 1.5](http://wsgi.readthedocs.io/en/latest/index.html). WSGI is the Web Server Gateway Interface. It is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.
4. [Django 1.7.1](https://www.djangoproject.com/). Hmm... I am still using an ancient version of Django. It is also because I wish I could have an exactly same developing environment with the deploy one. Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source. 

## Instructions

### Install Apache 2.4

Apache can be installed easily using the apt-get. `sudo apt-get install apache2`. Then we can use `apacheclt -v` to check the version of Apache and its success of installation.

### Install mod_wsgi 1.5
    
mod_wsgi can be installed using Pip, which can be installed using `sudo apt-get install python-pip`.

1. install mod_wsgi using `pip install mod_wsgi`. I met an error of `missing Apache httpd server packages.` here. I bypassed this error by `sudo apt-get install apache2-mpm-worker apache2-dev`.
2. download mod_wsgi-3.5.tar.gz from [here](http://modwsgi.readthedocs.io/en/latest/release-notes/version-3.5.html).
3. extract files from the package using `tar xvfz mod_wsgi-3.5.tar.gz`.
4. enter the directory `cd cd mod_wsgi-3.5`.
5. config by `./configure`
6. `make`
7. `sudo make install`

### Install Django 1.7.1

Install Django using command `pip install Django==1.7.1`. To verify its installation, try to `import django` in python console. If no error is raised, then the installation is successful. 

### Set up joshua_blog project with Apache

Note: after download the project, you should change the folder name to `joshua_blog`.

1. add the following code to the file of `/etc/apache2/apache2.conf`

        LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so
        WSGIScriptAlias / /home/joshua/CODE/PYTHON/joshua_blog/joshua_blog/wsgi.py
        Alias /media/ /home/joshua/CODE/PYTHON/joshua_blog/media/
        Alias /static/ /home/joshua/CODE/PYTHON/joshua_blog/static/

        <Directory /home/joshua/CODE/PYTHON/joshua_blog/static>
            Require all granted
        </Directory>

        <Directory /home/joshua/CODE/PYTHON/joshua_blog/media>
            Require all granted
        </Directory>

        <Directory /home/joshua/CODE/PYTHON/joshua_blog/joshua_blog>
            <Files wsgi.py>
                Require all granted
            </Files>
        </Directory>

        WSGIPythonPath /home/joshua/anaconda/lib/python2.7/site-packages
        ServerName localhost:80

2. add the following code to the file of `joshua_blog/joshua_blog/wsgi.py`

        import sys
        sys.path.append("/path/joshua_blog/")

    in my case, the path is `/home/joshua/CODE/PYTHON/`.

3. restart apache server by `sudo service apache2 restart`

### Install dependency modules
Coming here, we have set up the environment. But when we visit `127.0.0.1`, we found that the web server return 500 error. It is because several modules needed by joshua_blog are of need to be installed manually. We can see which modules are missed in the file of `/var/log/apache2/error.log`. Next we will see how to install these modules.

1. **django-bootstrap**. The author suggests to install this app using `pip install django-bootstrap`, but the latest version of the app requires Django>=1.8. Thus we need to download django-bootstrap from 6.x.x branch, which can be found [here](https://pypi.python.org/pypi/django-bootstrap3/6.2.0). Extract the package and enter its directory. Install by `python setup.py install`.
2. **django-filemanager**. The installation instruction can be found [here](http://joshua881228.webfactional.com/blog_using-imgiitroorkee-django-filemanager_59/).
3. **django-disqus**. Install by `pip install django-disqus`. A brief introduction in Chinese can be found [here](http://joshua881228.webfactional.com/blog_li-yong-disquskuai-su-da-jian-ping-lun-xi-tong_57/)
4. **unidecode**. Install by `pip install unidecode`.
5. **markdown2**. Install by `pip install markdown2`. A brief introduction in Chinese can be found [here](http://joshua881228.webfactional.com/blog_zai-djangogong-cheng-zhong-shi-yong-markdown_41/).

At last we can visit our website at 127.0.0.1. We can log in as the supervisor using the username of `joshua` and the password of `joshua`. We may meet other issues:

1. Here maybe we will get an error message reading "attempt to write a readonly database". We should change its mode by 'chmod 666 db.sqlite3'.
2. Then another error comes as "unable to open database file". Then we should change the owner of the the whole project `sudo chown www-data joshua_blog`.