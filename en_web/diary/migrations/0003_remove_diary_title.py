# Generated by Django 4.1 on 2022-08-13 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_diary_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='title',
        ),
    ]
