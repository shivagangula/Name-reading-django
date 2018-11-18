from django.shortcuts import render
from .models import singup_model
import nameread

def user(request):
    username = request.GET['username']
    password = request.GET['password']
    mobile_number = request.GET['mobile_number']
    email = request.GET['email']
    user  = singup_model(
                username = username,
                password=password,
                mobile_number = mobile_number,
                email = email
                )
    user.save()
    return render(request, 'login_logout/signin.html')


def signup(request):
    return render(request, 'login_logout/signup.html')


def signin(request):
    return render(request, 'login_logout/signin.html')
