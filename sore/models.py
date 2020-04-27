from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.urls import reverse


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