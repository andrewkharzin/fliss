from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from apps.users.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField
from thumbnails.fields import ImageField
from django.utils.html import escape
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from apps.organizations.models import Organization


class Agent(models.Model):
    TYPE_OF_AGENT = (
        ('Airline', 'Airline'),
        ('Airport', 'Airport'),
        ('GHA', 'GHA'),
        ('GSA', 'GSA')

    )
    type_of_agent = models.CharField(
        null=False, max_length=10, blank=False, choices=TYPE_OF_AGENT)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    organization_name = models.ForeignKey(
        Organization, on_delete=models.CASCADE)
    position = models.CharField(max_length=55, null=True, blank=True)
    # Organization = models.ForeignKey()
