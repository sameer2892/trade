from django.shortcuts import get_object_or_404, render
from .models import User

def index(request):
    return render(request, 'loginapp/index.html')

def signup(request):
    new_user = User()
    return render(request, 'loginapp/signup.html', {'new_user': new_user})

def signin(request):
    return render(request, 'loginapp/signin.html')

def navbar(request):
    return render(request, 'loginapp/navbar.html')

def register(request, new_user):
    if request.POST:
        new_user.name = request.POST['name']
        new_user.email = request.POST['email']
        new_user.contact = request.POST['contact']
        new_user.password = request.POST['password']
        new_user.save()
        return render(request, 'loginapp/signin.html')
    else:
        return render(request, 'loginapp/signup.html')


