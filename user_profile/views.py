from django.db import connection
from django.shortcuts import render
from user.Opreations.signin import md5_for_profile

# Create your views here.
from user_profile.oparations.profilequery import pro_query

user_id = []
def profile(request):
    send = pro_query(md5_for_profile[0])
    return render(request,'user_profile/Profile.html',send)


