from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.test import RequestFactory
from main.views import crawl


@shared_task
def add(x, y):
    return x + y

@shared_task
def start_spider():
    factory = RequestFactory()
    r = factory.post('')
    crawl(r)
