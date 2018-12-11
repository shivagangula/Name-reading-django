from django.db import connection
from django.shortcuts import render
from django.utils import timezone

from user.Opreations.signin import md5_for_profile, pk
from user.models import user_singup_model
from user_profile.models import StringsTable

# Create your views here.


def home(request):
        send = {'info':'login frist'}
        return render(request, 'user/signin.html',send)
def resultsend(request):
        add = request.GET['final_name']
        pkv = pk[0]
        user = user_singup_model.objects.get(pk = pkv)
        strings = StringsTable.objects.create(Strings=add,serched_date=timezone.now())
        strings.user.add(user)
        send = {'name':request.GET['final_name']}
        return render(request,'nr_game/Result.html',send)

def logout(request):
        return render(request, 'user/signin.html')
