from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def test1(request):
    return HttpResponse('This is test1 single view')