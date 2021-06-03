from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from apps.profiles.models import Profile


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class ProfileInline(admin.StackedInline):
    model = Profile  # specify the profile model
    can_delete = False  # prohibit removal
    # Specify which field to display, again avatar tag
    fields = ('avatar_tag',)
    readonly_fields = ['avatar_tag']  # Specify that this read only field


class EUserAdmin(UserAdmin):
    # Specify what will be in the form of inline
    inlines = [
        ProfileInline
    ]
    # modify the list of displayed fields to see the avatar with the other fields
    list_display = ('avatar_tag',) + CustomUserAdmin.list_display

    # and also create a method for getting the avatar tag from the user profile
    def avatar_tag(self, obj):
        return obj.userprofile.avatar_tag()


admin.site.register(CustomUser, CustomUserAdmin)
