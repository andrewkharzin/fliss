from django.db import models
from apps.users.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from thumbnails.fields import ImageField
from django.utils.html import escape
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


def upload_to(instance, filename):
    return 'avatars/%s' % filename


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=55, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(
        verbose_name=_('Avatar'), upload_to='userprofilesphoto', null=True, blank=True
    )

    @receiver(post_save, sender=CustomUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=CustomUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    # Here I return the avatar or picture with an owl, if the avatar is not selected

    def get_avatar(self):
        if not self.avatar:
            return '/static/images/default_user.png'
        return self.avatar.url

    # method to create a fake table field in read only mode
    def avatar_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.get_avatar())

    avatar_tag.short_description = 'Avatar'
