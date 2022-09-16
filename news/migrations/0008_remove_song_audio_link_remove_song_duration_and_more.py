# Generated by Django 4.0.4 on 2022-06-26 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='audio_link',
        ),
        migrations.RemoveField(
            model_name='song',
            name='duration',
        ),
        migrations.AddField(
            model_name='song',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
