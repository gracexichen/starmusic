# Generated by Django 4.0.5 on 2022-08-13 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='genre',
            field=models.CharField(default='multi', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='songs',
            name='file',
            field=models.FileField(upload_to='songs/'),
        ),
    ]
