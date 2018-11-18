from django.shortcuts import render
import random

# Create your views here.
def index(request):
    username = request.GET['username']
    password = request.GET['password']
    list1 = ["A","B","C","D","E"]
    list2 =["F","G","H","I","J"]
    list3 =["P","Q","R","S","T"]
    list4 =["U","V","W","X","Y"]
    list5 =["Z"," "," "," "," "]
    sendble_data = {
             'title':string,
             'list1':list1,
             'list2':list2,
             'list3':list3,
             'list4':list4,
             'list5':list5
             }
    if username == 'shiva' and password == '123' :
         return render(request, 'nameread/index.html', sendble_data)
