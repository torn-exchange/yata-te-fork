# Generated by Django 3.0.4 on 2020-06-14 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0054_playerdata_uidban'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='botPerm',
        ),
    ]
