# Generated by Django 2.2.5 on 2022-04-02 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220316_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avater',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
    ]
