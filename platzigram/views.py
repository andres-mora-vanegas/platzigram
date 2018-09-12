from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
import json

def hello_world(request):
    return HttpResponse('hello, world the time is {now}'.format(now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))

def hi(request):
    numbers=sorted(request.GET['numbers'].split(','))
    import pdb;pdb.set_trace() 
    response = JsonResponse([numbers],safe=False)
    return response

def sorted(request):
    numbers=[int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints=sorted(numbers)
    data={
        'status':'ok',
        'numbers':sorted_ints,
        'message':'Ingeners sorted succesfully'
    }
    
    return HttpResponse(json.dumps(data,indent=4),content_type='application/json')

def say_hy(request,name,age):
    if age<12:
        message='sorry {}, you are not allowed here'.format(name)
    else:
        message='hi {}, you are welcome'.format(name)
    return HttpResponse(message)
