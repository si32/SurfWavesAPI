from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import json
from django.http import JsonResponse
from urllib.parse import urlparse
from scrapyd_api import ScrapydAPI
from .models import DewataItem
from datetime import date


# Scrapyd api connect
scrapyd = ScrapydAPI('http://127.0.0.1:6800')


# Create your views here.
def index(request):
    # last 3 data rows
    last_data = DewataItem.objects.all().order_by('-date')[0:3]

    return render(request, 'index.html', {
        'last_update': last_data[0].date,
        'last_data': last_data
    })


def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url) # check if url format is valid
    except ValidationError:
        return False

    return True


# Start spyder to crawl
@csrf_exempt
@require_http_methods(['POST', 'GET']) # only get and post
def crawl(request):
    if request.method == 'POST':
        # start spider
        task = scrapyd.schedule('default', 'dewata_spider')

        return JsonResponse({'task_id': task, 'status': 'started'})

    # Get requests are for getting result of a specific crawling task
    elif request.method == 'GET':

        task_id = request.GET.get('task_id', None)

        if not task_id:
            return JsonResponse({'error': 'Missing args'})

        status = scrapyd.job_status('default', task_id)
        if status == 'finished':
            try:
                # this is the unique_id that we created even before crawling started.
                items = DewataItem.objects.all()
                result = {i: item.to_dict for i, item in enumerate(items)}
                return JsonResponse(result)
            except Exception as e:
                return JsonResponse({'error': str(e)})
        else:
            return JsonResponse({'status': status})
