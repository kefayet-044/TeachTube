# Generated by Django 3.1.3 on 2022-09-22 09:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.ManyToManyField(default=None, related_name='views', to=settings.AUTH_USER_MODEL),
        ),
    ]
