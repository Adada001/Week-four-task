# Generated by Django 4.1.3 on 2022-11-05 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0017_rename_song_id_lyric_song_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lyric',
            old_name='song_name',
            new_name='song_id',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='artiste_name',
            new_name='artiste_id',
        ),
    ]
