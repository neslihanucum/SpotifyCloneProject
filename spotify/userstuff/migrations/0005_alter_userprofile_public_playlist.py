# Generated by Django 3.2 on 2023-06-01 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstuff', '0004_auto_20230601_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='public_playlist',
            field=models.ManyToManyField(related_name='public_playlist', to='userstuff.Song'),
        ),
    ]