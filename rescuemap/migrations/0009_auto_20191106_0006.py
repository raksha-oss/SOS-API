# Generated by Django 2.2.6 on 2019-11-05 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rescuemap', '0008_auto_20191105_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='victim',
            name='time',
        ),
        migrations.AddField(
            model_name='victim',
            name='time_of_creation',
            field=models.DateTimeField(null=True),
        ),
    ]
