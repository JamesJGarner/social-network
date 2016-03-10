# Social Network Project
A social network using Django and PostgreSQL.


### Requirements

* Python 2.7.11
* PostgreSQL
* Git


### Installation

##### If using Windows:
Download and Install: https://www.microsoft.com/en-us/download/details.aspx?id=44266

 
```sh
$ git clone https://github.com/JamesJGarner/social-network
$ cd social-network
```

Create local.py in /social_network/settings/

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '' # Add in your own
DEBUG = True
```
Once you've filled out the file with your settings run these commands:
```sh
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
```