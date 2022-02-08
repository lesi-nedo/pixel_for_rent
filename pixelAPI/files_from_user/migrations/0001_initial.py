# Generated by Django 3.2 on 2021-04-22 20:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import files_from_user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_to_eval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=files_from_user.models.custom_dir, validators=[django.core.validators.FileExtensionValidator(['JPEG', 'PNG', 'GIF', 'JPG', 'TIFF', 'EPS', 'RAW'], "Please upload an image with one of     the following extensions 'JPEG', 'PNG', 'GIF', 'JPG', 'TIFF', 'EPS', 'RAW'")], verbose_name='file uploaded')),
                ('date_up', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='when was uploaded')),
                ('is_auth', models.BooleanField(default=False, help_text='True if the user is part of our community i.e registered.', verbose_name='User Is Authenticated')),
                ('user', models.ForeignKey(blank=True, help_text='User Thar uploaded file.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='File')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
            },
        ),
    ]