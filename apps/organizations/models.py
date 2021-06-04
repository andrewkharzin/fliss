from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from apps.users.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField
from thumbnails.fields import ImageField
from django.utils.html import escape
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


def upload_to(instance, filename):
    return 'avatars/%s' % filename


class Organization(models.Model):
    COMPANY_TYPE = (
        ('GHA', 'GHA'),
        ('GSA', 'GSA'),
        ('Airline', 'Airline')

    )
    org_title = models.CharField(
        max_length=55, null=True, blank=True, verbose_name=_('Name of company'))
    org_type = models.CharField(
        max_length=10, null=True, blank=True, choices=COMPANY_TYPE, verbose_name=_('Type'))
    org_logo = models.ImageField(
        upload_to='org_logos', null=True, blank=True, verbose_name=_('Company logo'))
    contact_phone = PhoneNumberField(verbose_name=_('Contact phone'))
    location = models.CharField(max_length=255, blank=True, null=True)
    About = models.TextField(null=True)

    def get_orglogo(self):
        if not self.org_logo:
            return '/static/images/org_default_logo.png'
        return self.org_logo.url

    # method to create a fake table field in read only mode
    def orglogo_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.get_orglogo())

    orglogo_tag.short_description = 'Org_logo'
