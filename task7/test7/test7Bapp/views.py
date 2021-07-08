from django.shortcuts import render, HttpResponse

# Create your views here.
def mul1view1(request):
    return HttpResponse('This is Task7 MultiViews app1 Views1')

def mul1view2(request):
    return HttpResponse('This is Task7 MultiViews2 app1 views2')