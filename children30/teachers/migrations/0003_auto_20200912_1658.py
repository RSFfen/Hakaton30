# Generated by Django 2.2.7 on 2020-09-12 13:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teachers', '0002_auto_20200912_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='owner',
        ),
        migrations.AddField(
            model_name='course',
            name='owner',
            field=models.ManyToManyField(blank=True, related_name='courses_created', to=settings.AUTH_USER_MODEL, verbose_name='Владелец курса:'),
        ),
    ]
