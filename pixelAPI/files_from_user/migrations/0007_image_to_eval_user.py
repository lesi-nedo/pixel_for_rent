# Generated by Django 3.2 on 2021-04-22 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files_from_user', '0006_remove_image_to_eval_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_to_eval',
            name='user',
            field=models.ForeignKey(default=None, help_text='User That uploaded file.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]