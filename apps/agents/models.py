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
    org_title = models.CharField(max_length=55, null=True, blank=True)
    org_logo = models.ImageField(
        verbose_name=_('Org_Logo'), upload_to='org_logos', null=True, blank=True
    )
    contact_phone = PhoneNumberField()

    def get_orglogo(self):
        if not self.org_logo:
            return '/static/images/org_default_logo.png'
        return self.org_logo.url

    # method to create a fake table field in read only mode
    def orglogo_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.get_orglogo())

    orglogo_tag.short_description = 'Org_logo'

    # def get_org_logo(self):
    #     if not self.avatar:
    #         return '/static/images/org_default_logo.png'
    #     return self.avatar.url

    # # method to create a fake table field in read only mode
    # def org_logo_tag(self):
    #     return mark_safe('<img src="%s" width="50" height="50" />' % self.get_org_logo())

    # org_logo_tag.short_description = 'Org_Logo'


class Consumer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    organization_name = models.ForeignKey(
        Organization, on_delete=models.CASCADE)
    position = models.CharField(max_length=55, null=True, blank=True)


class Agent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    organization_name = models.ForeignKey(
        Organization, on_delete=models.CASCADE)
    position = models.CharField(max_length=55, null=True, blank=True)
