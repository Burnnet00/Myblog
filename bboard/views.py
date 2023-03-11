from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('there will be boards')


# Create your views here.
