#coding: utf-8
# Django settings for stigull project.

CREATED_YEAR = 2007 #For copyright tag from templatetools

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    (u'Jóhann Þorvaldur Bergþórsson', 'johann.thorvaldur@gmail.com'),
    (u'Helgi Freyr Rúnarsson', 'helgi.runarsson@gmail.com'),
)

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = "stigull@hi.is"
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_HOST = "smtp.hi.is"
EMAIL_HOST_USER = "stigull"
EMAIL_HOST_PASSWORD = "9sKvsjRB"
EMAIL_SUBJECT_PREFIX = "[Stigull] "
EMAIL_USE_TLS = True

INTERNAL_IPS = ('127.0.0.1',)

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'stigull'
DATABASE_USER = 'stigull'
DATABASE_PASSWORD = 'H4sselhoff'
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = 'Atlantic/Reykjavik'
DATE_FORMAT = "d.m.Y"
DATETIME_FORMAT = "d.m.Y H:i"
TIME_FORMAT = "H:i"

LANGUAGE_CODE = 'is'

ugettext = lambda s: s
LANGUAGES = (
  ('is', ugettext('Icelandic')),
  ('en', ugettext('English')),
)


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/var/www/stigull/skrar/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/skrar/'
MEDIA_DESIGN_URL = 'myndir/honnun/' #No preceding slash

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/skrar/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '6tw8$$rb!*swkk4%bq%&b00(9%%@)s2=87*k$l7vhoorim=dy+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'pagination.middleware.PaginationMiddleware',

    'djangologging.middleware.LoggingMiddleware',
    'stigull.middleware.FileLoggingMiddleware'

)

ROOT_URLCONF = 'stigull.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    #'student.context_processors.info_name_processor',
)

TEMPLATE_DIRS = (
    '/home/johannth/programming/python/stigull/templates/',

)

INSTALLED_APPS = (
    #Core applications
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',

    #Extended core applications
    'django_extensions',
    'djangologging',
    #'compress',
    'templatetools',

    #User profiles
    #'user_profile',
    #'stigull_profile',
    #'django.contrib.comments',
    #'comment_utils',
    #'stigull',

    #'user_profile',
    #'phonebook',
    #'pagination',
    #'student',
    #'laws',
    #'news',
    #'navigation',
    #'djangodblog',
    #'xkcd',
)

AUTH_PROFILE_MODULE = 'stigull_profile.StigullUserProfile'
PROFILE_BASE = 'stigull_user_profile/profile_base.html'
EXTENDS_FROM = 'phonebook/phonebook_base.html'
LOGIN_URL = '/nemendur/innskraning/'
LOGOUT_URL = '/nemendur/utskraning/'
LOGIN_REDIRECT_URL = '/'

#START: Display images
DISPLAY_IMAGES_FOLDER = "myndir/simaskra/"
DISPLAY_IMAGE_SIZE = {'small': (30, 34) , 'medium': (75, 84), 'large': (150,168) }
DISPLAY_IMAGE_DEFAULT = "/var/www/stigull/skrar/myndir/simaskra/engin-mynd.jpg"

ABSOLUTE_URL_OVERRIDES = {
    'auth.user' : lambda user: "/nemendur/%s/" % user.username,
}

NAVIGATION = [(u'Heim', 'index'), (u'Fréttir', 'news_entry_archive_index'), (u'Símaskrá', 'phonebook'), (u'Um Stigul', 'info_show')]

#START: Settings for django-logging
LOGGING_LOG_SQL = DEBUG
LOG_FILENAME = '/var/log/stigull/stigull.log'
#END: Settings for django-logging

#START: Settings for django-compress
COMPRESS_VERSION = True
COMPRESS_CSS = {
    'stigull': {
        'source_filenames': ('css/reset.css',
                            'css/fonts-reset.css',
                            'css/layout.css',
                            'css/design.css',
                            'css/forms.css',
                            'css/phonebook-search.css'),
        'output_filename': 'css/stigull_compressed_?.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'frontpage': {
        'source_filenames': ('css/frontpage.css', ),
        'output_filename': 'css/stigull_frontpage_?.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'news': {
        'source_filenames': ('css/news.css',),
        'output_filename': 'css/stigull_news_compressed_?.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'phonebook': {
        'source_filenames': ('css/phonebook.css',),
        'output_filename': 'css/stigull_phonebook_compressed_?.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    }
}

COMPRESS_JS = {
    'jquery': {
        'source_filenames': ('js/jquery-1.2.6.min.js','js/jquery.taconite.js', 'js/jquery.validate.js' ),
        'output_filename': 'js/jquery_compressed_?.js',
    },
    'all': {
        'source_filenames': ('js/utils.js', 'js/phonebook.js', 'js/login-form.js' ),
        'output_filename': 'js/all_compressed_?.js',
    },
    'news': {
        'source_filenames': ('js/news.js', 'js/comments.js'),
        'output_filename': 'js/stigull_news_compressed_?.js',
    }
}
#END: Settings for django-compress


