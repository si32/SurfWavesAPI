from django.core.management.base import BaseCommand, CommandError
import requests
from django.http import HttpRequest
from django.test import RequestFactory
from main.views import crawl

class Command(BaseCommand):
    args = ''
    help = 'Export data from remote server'

    def handle(self, *args, **options):
        factory = RequestFactory()
        r = factory.post('')
        crawl(r)
