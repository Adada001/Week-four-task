# Generated by Django 4.1.3 on 2022-11-03 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0015_rename_lyrics_lyric'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]