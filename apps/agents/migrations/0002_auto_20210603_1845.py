# Generated by Django 3.2.3 on 2021-06-03 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumer',
            name='organization_name',
        ),
        migrations.RemoveField(
            model_name='consumer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Agent',
        ),
        migrations.DeleteModel(
            name='Consumer',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
    ]
