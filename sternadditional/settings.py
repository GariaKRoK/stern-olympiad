import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ''

DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    'USER': 'admin',
    'PASSWORD': 'admin_test',
    'HOST': 'localhost',
    'PORT': '',
    }
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sore',
    'widget_tweaks',
    'whitenoise',
    'tinymce'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'sternadditional.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sternadditional.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    }
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticprod"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#Payment olympiad
MERCHANT_ID = ''
#SECRET_KEY = ''
PRICE = str(500)
DESC = 'Оплата за олимпиаду'

#Email settings
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST =  'smtp.gmail.com'
EMAIL_HOST_USER = 'shtern.olymp@gmail.com'
EMAIL_HOST_PASSWORD = 'shternolymP1'

DICT_LINK_TIMER = {'1':'https://megatimer.ru/get/6367f9dffd3a5ed7dd51989ef0f17f11.js',
                        '2': 'https://megatimer.ru/get/6367f9dffd3a5ed7dd51989ef0f17f11.js',
                        '3': 'https://megatimer.ru/get/6367f9dffd3a5ed7dd51989ef0f17f11.js',
                        '4': 'https://megatimer.ru/get/7a48d044fc046ab345c035530eea8b64.js',
                        '5': 'https://megatimer.ru/get/650f9c317f032743cc744a6ade4e74c2.js',
                        '6': 'https://megatimer.ru/get/650f9c317f032743cc744a6ade4e74c2.js',
                        '7': 'https://megatimer.ru/get/650f9c317f032743cc744a6ade4e74c2.js',
                        '8': 'https://megatimer.ru/get/3a2a854aac4c5b0af1e735c018061189.js',}
DICT_BALLS = {'62': 2, '63': 2, '64': 2, '65': 2, '58': 2, '59': 2,
                  '66': 2, '47': 2, '48': 2, '50': 2, '49': 3, '51': 2,
                  '52': 2, '57': 3, '39': 3, '41': 2, '42': 2, '43': 2,
                  '44': 2, '33': 3, '34': 3, '35': 2, '36': 2, '25': 2,
                  '26': 2, '27': 2, '28': 2, '13': 2, '15': 2, '16': 2,
                  '17': 3, '19': 3, '5': 3, '6': 2, '7': 3, '8': 2, 
                  '10': 3, '11': 2, '68':3}