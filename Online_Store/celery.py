import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FirstShop.settings')
app = Celery('FirstShop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


