# Generated by Django 3.2.3 on 2021-06-04 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_auto_20210603_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='org_type',
            field=models.CharField(blank=True, choices=[('GHA', 'GHA'), ('GSA', 'GSA'), ('Airline', 'Airline')], max_length=10, null=True, verbose_name='Type'),
        ),
    ]
