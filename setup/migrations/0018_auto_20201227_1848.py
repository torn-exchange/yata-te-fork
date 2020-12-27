# Generated by Django 3.1.2 on 2020-12-27 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0017_dropletspec_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropletspec',
            name='disk',
            field=models.CharField(default='disk', max_length=64),
        ),
        migrations.AlterField(
            model_name='dropletspec',
            name='memory',
            field=models.CharField(default='memory', max_length=64),
        ),
        migrations.AlterField(
            model_name='dropletspec',
            name='name',
            field=models.CharField(default='name', max_length=64),
        ),
        migrations.AlterField(
            model_name='dropletspec',
            name='transfer',
            field=models.CharField(default='transfer', max_length=64),
        ),
        migrations.AlterField(
            model_name='dropletspec',
            name='vcpus',
            field=models.CharField(default='vcpus', max_length=64),
        ),
        migrations.AlterField(
            model_name='dropletspec',
            name='vpc_uuid',
            field=models.CharField(default='vpc_uuid', max_length=64),
        ),
        migrations.AlterField(
            model_name='paypal',
            name='endpoint',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='paypal',
            name='pwd',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='paypal',
            name='user',
            field=models.CharField(max_length=64),
        ),
    ]
