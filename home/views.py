from django.shortcuts import render


def index(request):
    """ To render Home page """
    
    return render(request, 'home/index.html')
