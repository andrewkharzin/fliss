# Generated by Django 3.2.3 on 2021-05-31 16:55

from django.db import migrations
import thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_photo',
            field=thumbnails.fields.ImageField(upload_to='userprofilesphoto'),
        ),
    ]
