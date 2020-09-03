from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.urls import reverse
from tinymce.models import HTMLField


class ClassNumber(models.Model):
    name = models.CharField('Номер класса', max_length=1)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Номер класса'
        verbose_name_plural = 'Номера классов'


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    telephone_number = models.CharField('Телефонный номер', max_length=12)
    class_number = models.ForeignKey(ClassNumber, on_delete=models.CASCADE, verbose_name='Номер класса')
    name_school = models.CharField('Название школы', max_length=50)
    count = models.IntegerField('Баллов за правильные ответы', default=0)
    paid = models.BooleanField('Оплачена ли олимпида', default=False)

    def __str__(self):
        return self.user.username
        
    class Meta:
        verbose_name = 'Школьник'
        verbose_name_plural = 'Школьники'

class CategoryEvent(models.Model):
    title = models.CharField(verbose_name='Название', primary_key=True, max_length=30)
    slug = models.SlugField(verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(verbose_name='Название', primary_key=True, max_length=50)
    slug = models.SlugField(verbose_name='Ссылка')
    main_image = models.ImageField(verbose_name='Заставка', upload_to='events/%Y/%m/%h/', blank=True)
    content = HTMLField(verbose_name='Контент', blank=True, null=True)
    short_description = HTMLField(verbose_name='Краткое описание', blank=True, null=True)
    data_created = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)
    data_event = models.DateTimeField(verbose_name='Дата мероприятия')
    #classes = models.ManyToManyField(Classes, verbose_name='Принимающие участие классы')
    is_active = models.BooleanField(default=True, verbose_name='Активность мероприятия')
    price = models.FloatField(verbose_name='Цены', blank=True, null=True, default=0)
    category = models.ForeignKey(CategoryEvent, on_delete=models.DO_NOTHING, verbose_name='Категория')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
    
    def __str__(self):
        return '{}. Категория: {}. Дата создания: {}. Дата проведения: {}'.format(self.title, 
                    self.category, self.data_created, self.data_event)
    
    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'category_slug': self.category.slug, 'slug': self.slug})

    def get_absolute_url_time_to_start(self):
        return reverse('time_to_start', kwargs={'category_slug': self.category.slug, 'slug': self.slug})


class UserInEvent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Пользователь')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие')
    paid = models.BooleanField(default=False, verbose_name='Оплатил ли пользователь участие')
    active = models.BooleanField(default=True, verbose_name='Будет ли принимать участие пользователь')
    date_registration = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации на мероприятие')

    class Meta:
        verbose_name = 'Пользователь, принимающий участие в мероприятии'
        verbose_name_plural = 'Пользователи, принимающие участие в мероприятиях'
    
    def __str__(self):
        return 'Пользователь {} {} в мероприятии {}. Оплата: {}.'.format(self.user.user.last_name, self.user.user.first_name, self.event, self.paid)


class Question(models.Model):
    class_number = models.ForeignKey(ClassNumber, on_delete=models.CASCADE, verbose_name='Номер класса')
    question = models.CharField('Вопрос', max_length=1000)
    image = models.ImageField('Фото', upload_to='pictures/', blank=True, null=True)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('answer', kwargs={'id': self.id})
        
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    text = models.CharField('Ответ', max_length=1000)
    correct = models.BooleanField('Верный ли ответ', default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        
class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    answer = models.CharField(verbose_name='Ответ', max_length=1000)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Школьник')

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователей'
