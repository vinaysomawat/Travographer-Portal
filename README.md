# Travographer-Portal
It is an implementation to Setup Amazon S3 in a Django Project, how to use S3 to handle user uploaded files.

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.1-brightgreen.svg)](https://djangoproject.com)

![Image](https://github.com/vinaysomawat/Travographer-Portal/blob/master/demo.png)


## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/sibtc/django-upload-example.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

You will need to install two Python libraries:

```bash
boto3
django-storages
```

The easiest way is to install the libraries using pip:

```bash
pip install boto3
pip install django-storages
```

Now add the storages to your INSTALLED_APPS inside the settings.py module:

### settings.py

```bash
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'storages',
]
```

This is the simplest use case. It works out-of-the-box with minimal configuration. All the configuration below goes inside the settings.py module:

### settings.py

```bash
AWS_ACCESS_KEY_ID = 'AKIAIT2Z5TDYPX3ARJBA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'sibtc-static'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'mysite/static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

**If you enjoy this project, please consider [supporting me](https://www.paypal.me/vinaysomawat) to continue developing and maintaining it.**

[![Support via PayPal](https://cdn.rawgit.com/twolfson/paypal-github-button/1.0.0/dist/button.svg)](https://www.paypal.me/vinaysomawat)