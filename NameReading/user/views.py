from django.shortcuts import render
from .models import user_singup_model
import nameread
from .md5_encript import convertmd5
from django.db import connection

def user(request):
    return render(request, 'user/signin.html')


def signup(request):
    return render(request, 'user/signup.html')


def signin(request):
    return render(request, 'user/signin.html')


def success(request):
    try:
      if request.GET['mobile_number'] != None:
          username = request.GET['username']
          password = request.GET['password']
          mobile_number = request.GET['mobile_number']
          email = request.GET['email']
          md5_hash = convertmd5(email)
          user  = user_singup_model(
                       username = username,
                       password=password,
                       mobile_number = mobile_number,
                       email = email,
                       md5_hash = md5_hash
                                )
          user.save()
          send ={'info':'registration success'}
          return render(request, 'user/success.html',send)
    except:
        try:
          email = request.GET['email']
          password = request.GET['password']
          md5_hash = convertmd5(email)
          cursor = connection.cursor()
          query ="""
                 SELECT md5_hash FROM user_user_singup_model
                 WHERE email= '{0}' and password = '{1}';
                 """.format(email,password)
          cursor.execute(query)
          row = cursor.fetchall()
          print(row)
          if md5_hash in row[0]:
             send = {'info':"user is there"}
             return render(request, 'user/success.html' ,send)
        except ValueError:
                send = {'info':"type correctly"}
                return render(request, 'user/success.html',send)
        except :
                send = {'info':"user is not there"}
                return render(request, 'user/success.html',send)
