# DEBUG = False
DEBUG = True
from settings import PROJECT_ROOT
from settings import DataBaseRouter
DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.mysql",
        # DB name or path to database file if using sqlite3.
        "NAME": "kinger",
        # Not used with sqlite3.
        "USER": "root",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "127.0.0.1",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "3306",
    },
    "master": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.mysql",
        # DB name or path to database file if using sqlite3.
        "NAME": "kinger",
        # Not used with sqlite3.
        "USER": "root",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "127.0.0.1",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "3306",
    },
    "slave": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.mysql",
        # DB name or path to database file if using sqlite3.
        "NAME": "kinger",
        # Not used with sqlite3.
        "USER": "root",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "127.0.0.1",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "3306",
    }        
}


    
DATABASE_ROUTERS = ''

#CACHE_BACKEND = 'caching.backends.memcached://192.168.1.222:11211/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache',
        'TIMEOUT': 3600*24*30
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
DEFAULT_FILE_STORAGE = 'oss_extra.storage.AliyunStorage'
THUMBNAIL_DEFAULT_STORAGE = 'oss_extra.storage.AliyunStorage'
THUMBNAIL_CHECK_CACHE_MISS = True
#GRIDFS_DATABASE = 'mongodb_storage'
OSS_ACCESS_KEY_ID = 'buRMMbpMqqOgp7ai'
OSS_SECRET_ACCESS_KEY = 'FT8DBVVMYG9UXg2DL3qEoZa3ytmoIT'
OSS_HOST = 'oss.aliyuncs.com'
OSS_HOST_INTER = 'oss.aliyuncs.com'
OSS_BUCKET = 'base01'

BROKER_URL = 'redis://localhost:6379/0'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'kinger.log': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_ROOT + "/../kinger.log",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'api': {
            'handlers': ['console', 'kinger.log'],
            'level': 'DEBUG',
        },
        'caching': {
            'handlers': ['console', 'kinger.log'],
            'level': 'DEBUG',
        },
    }
}
