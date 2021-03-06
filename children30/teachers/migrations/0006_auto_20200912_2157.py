# Generated by Django 2.2.7 on 2020-09-12 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import teachers.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teachers', '0005_auto_20200912_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ('text', 'video', 'image', 'file')}, on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType', verbose_name='Тип содержимого:'),
        ),
        migrations.AlterField(
            model_name='content',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contents', to='teachers.Module', verbose_name='Учебный модуль:'),
        ),
        migrations.AlterField(
            model_name='content',
            name='object_id',
            field=models.PositiveIntegerField(verbose_name='Идентификатор объекта:'),
        ),
        migrations.AlterField(
            model_name='content',
            name='order',
            field=teachers.fields.OrderField(blank=True, verbose_name='Порядковый номер:'),
        ),
        migrations.RemoveField(
            model_name='course',
            name='owner',
        ),
        migrations.AddField(
            model_name='course',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='courses_created', to=settings.AUTH_USER_MODEL, verbose_name='Владелец курса:'),
            preserve_default=False,
        ),
    ]
