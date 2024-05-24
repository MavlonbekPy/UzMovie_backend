from django.contrib import admin
from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')


admin.site.register(MyUser, MyUserAdmin)
