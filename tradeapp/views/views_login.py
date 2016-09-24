from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import re


def signup(request):

    context = {}
    user_object = request.user
    if user_object.is_authenticated:
        return HttpResponseRedirect('/home/')
    if request.POST:
        user_email = request.POST['email']
        user_pass = request.POST['password']
        user_name = request.POST['username']

        checkuser = User.objects.filter(username=user_name)

        if not checkuser:
            if not re.match(r'(?=.*[!@#$%^&*()_+=])(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}', user_pass):
                messages.warning(request, 'Wrong Password Format!!')
                return render(request, 'tradeapp/signup.html')

            user = User.objects.create_user(username=user_name, email=user_email, password=user_pass)
            userauth = authenticate(username=user_name, password=user_pass)
            if userauth:
                login(request, userauth)
                msg = "You have been logged in. Welcome %s" % user.username
                messages.warning(request, msg)
                return render(request, 'tradeapp/home.html')
        elif checkuser:

                messages.warning(request, 'Please choose different username')
                return render(request, 'tradeapp/signup.html',  context)

    return render(request, 'tradeapp/signup.html', context)


def home(request):
    return render(request, 'tradeapp/home.html')


@login_required(login_url='/signin/')
def user_logout(request):
    logout(request)

    messages.warning(request, 'Logged out. Please "Sign in" to view this page.')
    return HttpResponseRedirect('/home/')


def signin(request):

    user_object = request.user
    if user_object.is_authenticated:
        return HttpResponseRedirect('/home/')

    if request.POST:
        user_name = request.POST['username']
        user_pass = request.POST['password']
        user = authenticate(username=user_name, password=user_pass)

        if user:
            if user.is_active:
                login(request, user)
                msg = "You have been logged in. Welcome %s" % user.username
                messages.warning(request, msg)
                return render(request, 'tradeapp/home.html')
            else:
                messages.warning(request, 'Your account has been disabled.')
                return render(request, 'tradeapp/home.html')
        else:
            messages.warning(request, 'Wrong credentials.')
            return render(request, 'tradeapp/signin.html')

    return render(request, 'tradeapp/signin.html')


@login_required(login_url= '/signin/')
def edit_profile(request):
    if request.POST:
        user = request.user
        if request.POST['page'] == "password":
            pass1 = request.POST['new_pass']
            pass2 = request.POST['new_pass1']
            if pass1 == pass2:
                if not re.match(r'(?=.*[!@#$%^&*()_+=])(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}', pass1):
                    messages.warning(request, 'Wrong Password Format!!')
                    return render(request, 'tradeapp/edit_profile.html')

                user.set_password(pass1)
                user.save()
                messages.warning(request, 'Password changed successfully.')
                return HttpResponseRedirect('/signin/')
            else:
                messages.warning(request, 'Password do not match.')
                return render(request, 'tradeapp/edit_profile.html')
        elif request.POST['page'] == "details":
            user_name = request.POST['username']
            user_email = request.POST['email']

            if user_name != user.username:
                checkuser = User.objects.filter(username=user_name)
                if not checkuser:
                    user.username = user_name
                else:
                    messages.warning(request, 'This username is already taken. Please select a different username.')
                    return render(request, 'tradeapp/edit_profile.html')

            user.email = user_email
            user.save()
            messages.warning(request, 'Details updated successfully.')
            return render(request, 'tradeapp/edit_profile.html')

    return render(request, 'tradeapp/edit_profile.html')