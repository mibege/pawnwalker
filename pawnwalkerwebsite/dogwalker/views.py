from django.shortcuts import render

# Create your views here.


def registerUserDogWalker(request):
    template = 'dogwalkerregistration.html'
    return render(request,template,None)


def loginUserDogWalker(request):
    template = 'logindogWalker.html'
    return  render(request,template,None)