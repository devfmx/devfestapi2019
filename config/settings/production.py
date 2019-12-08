import environ
import dj_database_url


env = environ.Env()


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOST",default="*")

DATABASES = dict(default={})

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)



#S3 storage


GS_BUCKET_NAME = 'devfestcdmx2019'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME



STATICFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR),'website/static')
]

STATIC_ROOT = "/static/"



#STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
#MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

