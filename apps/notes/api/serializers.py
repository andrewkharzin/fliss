from django.db.models import fields
from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


from ..models import Note


class NoteSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'content',
            'tags',
            'access_level',
            'created_by',
            'created_at',
            'total_likes'
        )
