# Generated by Django 2.2.5 on 2022-04-02 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundings', '0012_auto_20220402_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='check_in',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='funding',
            name='check_out',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to=''),
        ),
    ]
