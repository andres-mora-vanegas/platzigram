from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime

def hello_world(request):
    return HttpResponse('hello, world the time is {now}'.format(now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))

def hi(request):
    numbers=sorted(request.GET['numbers'].split(','))
    response = JsonResponse([numbers],safe=False)
    return response