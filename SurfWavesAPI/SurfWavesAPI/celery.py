from __future__ import absolute_import, unicode_literals
from django.conf import settings

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SurfWavesAPI.settings')

app = Celery('SurfWavesAPI')
app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()
