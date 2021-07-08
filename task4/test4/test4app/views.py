from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def urls4(request):
    return HttpResponse('This is task4 URLS using Include')