from django.db import models
from apps.users.models import CustomUser
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from apps.likes.models import Like


# class SharedNotes(models.Model):
#     " Keeps track of who shares what to whom, and when "
#     created_at = models.DateTimeField(auto_now_add=True)
#     box = models.ForeignKey(Box)
#     seller = models.ForeignKey(Seller)
#     customer = models.ForeignKey(Customer)

class Note(models.Model):
    ACCESS_PUBLIC = 0
    ACCESS_PRIVATE = 1
    ACCESS_LEVEL_CHOICES = [
        (ACCESS_PUBLIC, 'Public'),
        (ACCESS_PRIVATE, 'Private')
    ]

    title = models.CharField(max_length=55, null=True, blank=True, default='')
    content = models.TextField()
    tags = TaggableManager(blank=True)
    access_level = models.IntegerField(
        choices=ACCESS_LEVEL_CHOICES, default=ACCESS_PRIVATE)

    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = GenericRelation(Like)

    # Sharing system (User can share any note )
    # shared_with = ManyToManyField(CustomUser,
    #                               related_name = 'sharing_to_user', through = SharedNotes)

    def __STR__(self):
        return self.title + " " + self.created_by + " " + self.created_at + " " + self.access_level + " " + self.tags

    @ property
    def total_likes(self):
        return self.likes.count()

    def get_tags_display(self):
        return self.tags.values_list('name', flat=True)
