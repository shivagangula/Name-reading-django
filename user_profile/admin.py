from django.contrib import admin
from .models import StringsTable

# Register your models here.
class StringsAdmin(admin.ModelAdmin):
    list_display = ['Strings','serched_date']
admin.site.register(StringsTable,StringsAdmin)