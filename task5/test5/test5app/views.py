from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def msg(request):
    return render(request, 'msg.html')