# Generated by Django 3.2 on 2021-04-22 22:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files_from_user', '0003_auto_20210422_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_to_eval',
            name='date_up',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='when was uploaded'),
        ),
        migrations.AddField(
            model_name='image_to_eval',
            name='user',
            field=models.ForeignKey(blank=True, default=None, help_text='User Thar uploaded file.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='File'),
        ),
    ]
