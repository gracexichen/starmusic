# Generated by Django 4.0.5 on 2022-08-13 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('artist', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to='images/')),
                ('file', models.FileField(upload_to='musics/')),
            ],
        ),
    ]
