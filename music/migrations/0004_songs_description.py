# Generated by Django 4.0.5 on 2022-09-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_songs_audio_alter_songs_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='description',
            field=models.TextField(default=None, max_length=800),
            preserve_default=False,
        ),
    ]
