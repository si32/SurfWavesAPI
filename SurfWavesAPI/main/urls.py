from django.urls import re_path, path
from main import views

urlpatterns = [
    re_path(r'^api/crawl', views.crawl, name='crawl'),
    path('', views.index, name='index'),
]
