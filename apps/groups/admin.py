from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group
from django.contrib import admin
from .models import CustomGroup


class GroupInline(admin.StackedInline):
    model = CustomGroup
    can_delete = False
    verbose_name_plural = 'custom groups'


class GroupAdmin(BaseGroupAdmin):
    inlines = (GroupInline, )


# Re-register GroupAdmin
admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
