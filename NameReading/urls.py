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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import user.views
import nr_game.views
import user_profile.views


urlpatterns = [
        url('^admin/', admin.site.urls),
        url('^signup/', user.views.signup, name='signup'),
        url('^$', user.views.signin, name='signin'),
        url('^signup_success/', user.views.signup_success, name='signup_success'),
        url('^signin_success/', user.views.signin_success, name='signin_success'),
        url('^nr_game/', nr_game.views.home, name = 'nr_game'),
        url('^Result/', nr_game.views.resultsend, name = 'result'),
        url('^profile/', user_profile.views.profile, name='profile'),
        url('^logout/', nr_game.views.logout, name='logout')

]
