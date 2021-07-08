from django.shortcuts import render, HttpResponse

# Create your views here.
def single(request):
    return HttpResponse('This is multiapp single view')