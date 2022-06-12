# Generated by Django 2.2.5 on 2022-04-12 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundings', '0014_auto_20220402_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funding',
            old_name='check_in',
            new_name='funding_end',
        ),
        migrations.RenameField(
            model_name='funding',
            old_name='check_out',
            new_name='funding_start',
        ),
        migrations.RenameField(
            model_name='funding',
            old_name='host',
            new_name='lyricist',
        ),
        migrations.RenameField(
            model_name='funding',
            old_name='baths',
            new_name='music_share',
        ),
        migrations.RenameField(
            model_name='funding',
            old_name='bedrooms',
            new_name='music_stock',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='address',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='amenities',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='beds',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='city',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='country',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='facilities',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='guests',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='house_rules',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='instant_book',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='music_type',
        ),
        migrations.AddField(
            model_name='funding',
            name='music_type',
            field=models.ManyToManyField(blank=True, related_name='fundings', to='fundings.MusicType'),
        ),
    ]
