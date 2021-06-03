from django.contrib import admin
from .models import Note
from apps.users.models import CustomUser
from apps.likes.models import Like


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'tags',
        'created_by',
        'access_level',
        'created_at',
        # 'likes',

    ]
