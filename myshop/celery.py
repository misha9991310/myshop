import os
from celery import Celery
from django.conf import settings

# Задаём переменную окружения, содержащую название файла настроек нашего проекта.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()