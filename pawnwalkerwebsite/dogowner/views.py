from django.shortcuts import render

# Create your views here.


def index(request):
    template = 'index.html'
    return render(request,template,None)


def registerUser(request):
    template = 'regisrationForm.html'
    return render(request,template,None)


def loginUser(request):
    template = 'login.html'
    return  render(request,template,None)