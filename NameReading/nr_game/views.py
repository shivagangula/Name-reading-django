from django.shortcuts import render

# Create your views here.
def home(request):
    pi = request.path_info
    if "c1c2066cf35fdfa32870797c1000114c" in pi[0]:
       return render(request, 'nr_game/index.html')
    else:
        send = {'info':'login frist'}
        return render(request, 'user/signin.html',send)