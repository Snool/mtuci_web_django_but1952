from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'static_handler.html', {'STATIC_URL': 'static/'})


def index_no_type(request):
    return HttpResponse(u'Hello, World')
