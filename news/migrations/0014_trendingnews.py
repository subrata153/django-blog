# Generated by Django 3.0.6 on 2020-07-23 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20200719_0437'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrendingNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tnews', models.CharField(default='-', max_length=200)),
            ],
        ),
    ]
