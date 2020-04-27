from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpStudentForm(forms.ModelForm):
    telephone_number = forms.CharField(max_length=11, help_text='Телефонный номер')
    class_number = forms.ModelChoiceField(queryset=ClassNumber.objects.all(), help_text='Год обучения')
    name_school = forms.CharField(max_length=50, help_text='Название текущего учебного заведения')

    class Meta:
        model = Student
        fields = ['telephone_number', 'class_number',
                  'name_school']

class SignUpUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email',
                'first_name', 'last_name',
                'password1', 'password2']
                
class UserAnswerForm(forms.ModelForm):
    class Meta:
        model = UserAnswer
        fields = ['answer']

class UserAnswerForm68(forms.Form):
    q681 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q682 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q683 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q684 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')

class UserAnswerForm38(forms.Form):
    q381 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q382 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q383 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')

class UserAnswerForm48(forms.Form):
    q481 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q482 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')

class UserAnswerForm29(forms.Form):
    q291 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q292 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q293 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')

class UserAnswerForm32(forms.Form):
    q321 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q322 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')

class UserAnswerForm45(forms.Form):
    q451 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q452 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q453 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q454 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q455 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q456 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')

class UserAnswerForm23(forms.Form):
    q231 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q232 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q233 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q234 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')
    q235 = forms.CharField(max_length=100, help_text='Введите ваш ответ: ')