# Generated by Django 4.1 on 2022-08-13 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='title',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]