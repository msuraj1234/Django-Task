from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('This is first views task2')
def info(request):
    return HttpResponse('This is second view views task2')