from django.shortcuts import render
from user.Opreations.signin import SignInQuery
from user.Opreations.signup import signup_qurey


def user(request):
    return render(request, 'user/signin.html')


def signup(request):
    return render(request, 'user/signup.html')


def signin(request):
    return render(request, 'user/signin.html')


def signup_success(request):
    #getting requests from signup form
    username = request.GET['username']
    password = request.GET['password']
    mobile_number = request.GET['mobile_number']
    email = request.GET['email']




    #calling singup_qurey function from operation.signup package
    # it will return resonable output strings in the form of python
    #dictionary for furtur purpose
    recived_data = signup_qurey(username,password,mobile_number,email)




    #after recived dictionary.check is 'success' string is their
    #or not in recived dictionar if thier it redirect
    #login page
    if recived_data['info'] == "success":
      send = {'info':'your registration succesfull'}
      return render(request, 'user/signin.html', send)
    #if recived dictionay have no 'success' string it return
    #what problem is occured then showed current signup page
    else:
        return render(request, 'user/signup.html', recived_data)


def signin_success(request):



    # taking email and password from user signin form
        email = request.GET['email']
        password = request.GET['password']





    #calling signinquery() function from oparation package
    #it work same as singupquery() function
        recived_data = SignInQuery(email, password)






    #if success is their in recived_data it finally shows original page with user name
        if recived_data['info'] == 'success':
            return render(request, 'nr_game/index.html' ,recived_data)
    #else it shows what problem is occured in current signin page
        else:
            return render(request, 'user/signin.html', recived_data)