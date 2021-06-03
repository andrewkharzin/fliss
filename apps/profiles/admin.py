from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'phone_number',
        'birth_date',
        'email',
        'avatar_tag',


    ]
    readonly_fields = ('avatar_tag',)
