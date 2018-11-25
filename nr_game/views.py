from django.shortcuts import render

# Create your views here.


def home(request):
        send = {'info':'login frist'}
        return render(request, 'user/signin.html',send)


