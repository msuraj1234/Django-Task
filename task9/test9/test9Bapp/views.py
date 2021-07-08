from django.shortcuts import render, HttpResponse

# Create your views here.
def url9A1(request):
    return HttpResponse('This is multiapp app2 url-1')

def url9B2(request):
    return HttpResponse('This is multiapp app2 url-2')