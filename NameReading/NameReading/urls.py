"""NameReading URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import nameread.views
import user.views


urlpatterns = [
        path('admin/', admin.site.urls),
        path('read/', nameread.views.index, name='read'),
        path('signup/', user.views.signup, name='signup'),
        path('', user.views.signin, name='signin'),
        path('signup_success/', user.views.signup_success, name='signup_success'),
        path('signin_success/', user.views.signin_success, name='signin_success'),
]
