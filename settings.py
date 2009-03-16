import os

DEBUG = True

ROOT_URLCONF = 'urls'

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.middleware.doc.XViewMiddleware',
)

INSTALLED_APPS = ()

ROOT_PATH = os.path.dirname(__file__)

TEMPLATE_DIRS = (
	os.path.join(ROOT_PATH, 'templates'),
)

MEDIA_URL = '/meida/'

DELICIOUS_API_URL = 'feeds.delicious.com'

TEMPLATE_CONTEXT_PROCESSORS = ()

INSTALLED_APPS = ()