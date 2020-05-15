import os

from .base import CommunityBaseSettings

DATABASES = {
    'default': {
    	'ENGINE': 'django.db.backends.mysql',
        'NAME': 'readthedocs',
        'USER': 'root',  # Not used with sqlite3.
        'PASSWORD': '572136',
        'HOST': '192.168.1.6',
        'PORT': '3306',
    }

}


SLUMBER_USERNAME = 'aim'
SLUMBER_PASSWORD = os.getenv('RTD_SLUMBER_PASSWORD', '572136zhanghongs')
PRODUCTION_DOMAIN = 'www.aim-zj.xyz'
SECRET_KEY = 'changemeplease'
ALLOW_PRIVATE_REPOS = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
