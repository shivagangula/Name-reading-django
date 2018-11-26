from django.contrib import admin
from .models import user_singup_model


class modelclass(admin.ModelAdmin):
    list_display = ['username','password','mobile_number','email','md5_hash']
# Register your models here.
admin.site.register(user_singup_model,modelclass)
