Provisioning a new site
=======================

Hosting Service: Dreamhost

## Required packages

* Python 3.6
* Passenger
* virtualenv + pip
* Git

Installing Python in virtualenv:
    https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-Python-s-virtualenv-using-Python-3

You should install django first, and then upload repo:
    https://help.dreamhost.com/hc/en-us/articles/215317948-How-to-install-Django-using-virtualenv

    https://help.dreamhost.com/hc/en-us/articles/215319648-How-to-create-a-Django-project-using-virtualenv

edit passenger_wsgi.py:
    replace SITENAME
    replace VIRTUALENV
    lives in root of site

edit django settings.py:
    include sitename under HOSTS (add both www.SITENAME and SITENAME with no www)

database:
    migrate on server?

Static files go in:
    public/static/