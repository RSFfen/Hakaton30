from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField


class Subject(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Название дисциплины:')
    slug = models.SlugField(max_length=200, unique=True, verbose_name = 'url дисциплины:')

    class Meta:
        verbose_name_plural = 'Учебные дисциплины'
        verbose_name = 'Учебная дисциплина'
        ordering = ['title']


    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(User,
                              related_name='courses_created',
                              on_delete=models.DO_NOTHING, verbose_name = 'Владелец курса:' )
    subject = models.ForeignKey(Subject,
                                related_name='courses',
                                on_delete=models.DO_NOTHING, verbose_name = 'Учебная дисциплина:')
    title = models.CharField(max_length=200, verbose_name = 'Название курса:')
    slug = models.SlugField(max_length=200, unique=True, verbose_name = 'url курса:' )
    overview = models.TextField(verbose_name = 'Краткое описание курса:')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Учебные курсы'
        verbose_name = 'Учебный курс'
        ordering = ['-created']

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name = 'Название модуля:')
    description = models.TextField(blank=True,  verbose_name = 'Описание модуля:' )
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        verbose_name_plural = 'Учебные модули'
        verbose_name = 'Учебный модуль'

    class Meta:
            ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)

    def __str__(self):
        return self.title

EDU_KINDS = (
   ('0', 'ученик'),
   ('ж', 'преподаватель'),
)

class Profile(models.Model) :
    user = models.OneToOneField(User, on_delete = models.DO_NOTHING, related_name='profile')
    type = models.CharField(max_length=1, choices=EDU_KINDS, verbose_name = 'Тип участника:')  # 0 - ученик, 1 - учитель

    def __str__(self) :
        return 'Профиль для {}'.format(self.user.username)

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'
        ordering = ['user']

class Content(models.Model):
    module = models.ForeignKey(Module,
                               related_name='contents',
                               on_delete=models.DO_NOTHING, verbose_name = 'Учебный модуль:' )
    content_type = models.ForeignKey(ContentType,
                                     limit_choices_to={'model__in':('text',
                                                                    'video',
                                                                    'image',
                                                                    'file')},
                                     on_delete=models.DO_NOTHING, verbose_name = 'Тип содержимого:' )
    object_id = models.PositiveIntegerField(verbose_name = 'Идентификатор объекта:')
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'], verbose_name = 'Порядковый номер:'  )

    class Meta:
        verbose_name_plural = 'Темы обучения'
        verbose_name = 'Тема обучения'
#        ordering = ['order']

class ItemBase(models.Model):
    owner = models.ForeignKey(User,
                              related_name='%(class)s_related',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
       file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()
