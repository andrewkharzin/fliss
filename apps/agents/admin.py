from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Consumer, Agent, Organization


@admin.register(Consumer)
class ConsumerAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'organization_name',
        'position',

    ]


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'organization_name',
        'position',

    ]


@admin.register(Organization)
class OrgAdmin(admin.ModelAdmin):
    list_display = [
        'org_title',
        'contact_phone',
        'org_logo',
        'orglogo_tag'

    ]


class OrgInline(admin.StackedInline):
    model = Organization  # specify the profile model
    can_delete = False  # prohibit removal
    # Specify which field to display, again avatar tag
    fields = ('org_logo_tag',)
    readonly_fields = ['org_logo_tag']  # Specify that this read only field


class EOrgAdmin(UserAdmin):
    # Specify what will be in the form of inline
    inlines = [
        OrgInline
    ]
    # modify the list of displayed fields to see the avatar with the other fields
    # list_display = ('orglogo_tag') + OrgAdmin.list_display

    # and also create a method for getting the avatar tag from the user profile
    def orglogo_tag(self, obj):
        return obj.userprofile.get_orglogo()
