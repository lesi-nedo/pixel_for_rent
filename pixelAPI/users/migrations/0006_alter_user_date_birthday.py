# Generated by Django 3.2 on 2021-04-22 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210410_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_birthday',
            field=models.DateField(default='1900-01-01', verbose_name='Date Of Birth'),
        ),
    ]
