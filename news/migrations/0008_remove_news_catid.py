# Generated by Django 3.0.6 on 2020-06-09 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200609_0303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='catid',
        ),
    ]
