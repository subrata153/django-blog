# Generated by Django 3.0.6 on 2020-06-09 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subcat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='-', max_length=50)),
                ('catname', models.TextField(default='-', max_length=50)),
                ('catid', models.IntegerField(default=0)),
                ('description', models.TextField(default='-', max_length=500)),
            ],
        ),
    ]
