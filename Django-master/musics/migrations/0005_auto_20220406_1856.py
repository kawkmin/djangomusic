# Generated by Django 2.2.5 on 2022-04-06 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musics', '0004_auto_20220329_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='songwriter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='musics', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='music_photos'),
        ),
    ]
