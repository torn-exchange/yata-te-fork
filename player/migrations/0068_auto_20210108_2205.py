# Generated by Django 3.1.2 on 2021-01-08 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0067_auto_20210108_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='section',
            field=models.CharField(choices=[('all', 'all'), ('player', 'player'), ('bazaar', 'bazaar'), ('faction', 'faction'), ('target', 'target'), ('awards', 'awards'), ('stock', 'stock'), ('company', 'company'), ('loot', 'loot')], default='B', max_length=16),
        ),
    ]
