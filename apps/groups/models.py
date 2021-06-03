from django.db import models
from apps.users.models import CustomUser
from django.contrib.auth.models import Group, GroupManager


class CustomGroup(models.Model):
    """
    Overwrites original Django Group.
    """

    def __str__(self):
        return "{}".format(self.group.name)

    group = models.OneToOneField(
        'auth.Group', unique=True, on_delete=models.CASCADE)
    email_alias = models.EmailField(max_length=70, blank=True, default="")
