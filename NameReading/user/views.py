from django.shortcuts import render

from user.Opreations.md5_encript import convertmd5
from user.Opreations.signin import SignInQuery
from user.Opreations.signup import signup_qurey
from .models import user_singup_model
from django.db import connection

def user(request):
    return render(request, 'user/signin.html')


def signup(request):
    return render(request, 'user/signup.html')


def signin(request):
    return render(request, 'user/signin.html')


def signup_success(request):

    username = request.GET['username']
    password = request.GET['password']
    mobile_number = request.GET['mobile_number']
    email = request.GET['email']

    recived_data = signup_qurey(username,password,mobile_number,email)

    if recived_data['info'] == "success":
      send = {'info':'your registration succesfull'}
      return render(request, 'user/signin.html', send)

    else:
        return render(request, 'user/signup.html', recived_data)


def signin_success(request):
        email = request.GET['email']
        password = request.GET['password']
        recived_data = SignInQuery(email, password)
        if recived_data['info'] == 'success':
            send = {'info':'success'}
            return render(request, 'nr_game/index.html' ,send)
        else:
            return render(request, 'user/signin.html', recived_data)