from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    # add_form

    model = User
    list_display = ['username', 'email', 'is_staff']


admin.site.register(User, UserAdmin)
