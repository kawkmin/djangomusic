# Generated by Django 2.2.5 on 2022-04-12 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0005_auto_20220406_1856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='songwriter',
            new_name='lyricist',
        ),
    ]