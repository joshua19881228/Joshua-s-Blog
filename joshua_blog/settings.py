"""
Django settings for joshua_blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ADMINS = ('joshua1988', 'lizhixuan_1988@126.com',)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm3b54rbd_iu5n*u#vz-+@7cw#ah6*=8$q^4pr-si^^v9i)rr7#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Bootstrap for static-files
    'bootstrap3',
    # The APPS below are added by Joshua Li for blog#
    'app_blogs',
    'app_accounts',
    'django.contrib.sites',
    'disqus',
    'filemanager',
)

#SITE_ID = 1
DISQUS_API_KEY = 'WJsmS0hUZcMBIpRaJvDBMVoNe6ECB7jqCwL9rtozpBqjsiGHPht9dv8W7NJ4Li0I'
DISQUS_WEBSITE_SHORTNAME = 'joshualiblog'

MIDDLEWARE_CLASSES = (
	'joshua_blog.middleware.WebFactionFixes',	
	###
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'joshua_blog.urls'

WSGI_APPLICATION = 'joshua_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SITE_ID = 1

STATIC_URL = 'http://127.0.0.1/static/'
STATIC_ROOT = '/home/joshua/CODE/PYTHON/joshua_blog/static/'
MEDIA_URL = 'http://127.0.0.1/media/'
MEDIA_ROOT = '/home/joshua/CODE/PYTHON/joshua_blog/media/'

FILEMANAGER_UPLOAD_ROOT = MEDIA_ROOT + 'uploads/'
FILEMANAGER_UPLOAD_URL = MEDIA_URL + 'uploads/'

# bootstrap settings
BOOTSTRAP3 = {
    # The URL to the jQuery JavaScript file
    'jquery_url': '//code.jquery.com/jquery.min.js',
    # The Bootstrap base URL
    'base_url': '//netdna.bootstrapcdn.com/bootstrap/3.2.0/',
    # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
    'css_url': None,
    # The complete URL to the Bootstrap CSS file (None means no theme)
    'theme_url': None,
    # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
    'javascript_url': None,
    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap3.html)
    'javascript_in_head': False,
    # Include jQuery with Bootstrap JavaScript (affects django-bootstrap3 template tags)
    'include_jquery': False,
    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-2',
    # Field class to use in horiozntal forms
    'horizontal_field_class': 'col-md-4',
    # Set HTML required attribute on required fields
    'set_required': True,
    # Set placeholder attributes to label if no placeholder is provided
    'set_placeholder': True,
    # Class to indicate required (better to set this in your Django form)
    'required_css_class': '',
    # Class to indicate error (better to set this in your Django form)
    'error_css_class': 'has-error',
    # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    'success_css_class': 'has-success',
    # Renderers (only set these if you have studied the source and understand the inner workings)
    'formset_renderers':{
        'default': 'bootstrap3.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap3.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap3.renderers.FieldRenderer',
        'inline': 'bootstrap3.renderers.InlineFieldRenderer',
    },
}


# Template files
TEMPLATE_DIRS = ( os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, os.path.join('templates', 'include')), )
