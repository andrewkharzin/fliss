from django.contrib import admin
from .models import Organization


@admin.register(Organization)
class OrgAdmin(admin.ModelAdmin):
    list_display = [
        'org_title',
        'org_type',
        'contact_phone',
        'orglogo_tag'

    ]
