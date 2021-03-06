# Generated by Django 3.2.3 on 2021-06-03 18:48

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_title', models.CharField(blank=True, max_length=55, null=True)),
                ('org_logo', models.ImageField(blank=True, null=True, upload_to='org_logos', verbose_name='Org_Logo')),
                ('contact_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
    ]
