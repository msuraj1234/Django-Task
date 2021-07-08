from django.shortcuts import render, HttpResponse

# Create your views here.
def url9A(request):
    return HttpResponse('This is multiapp app1 url-1')

def url9B(request):
    return HttpResponse('This is multiapp app1 url-2')