from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.http import HttpResponse, Http404, JsonResponse
from .forms import *
from .models import *
from hashlib import sha256
from urllib.parse import urlencode, parse_qsl
import json
import datetime
from django.contrib.auth import logout

def auth_user(request):
    """
        signin view
        using django authenticate mechanism
    """
    if request.method == 'POST':
        if 'password22' in request.POST:
            username = request.POST.get('username22')
            password = request.POST.get('password22')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('payment')
            else:
                messages.info(request, 'Неверный логин или пароль')
                return redirect('auth_user')
        else:
            if User.objects.filter(username=request.POST.get('username')).exists():
                    messages.info(request, 'Логин уже занят')
            elif User.objects.filter(email=request.POST.get('email')).exists():
                messages.info(request, 'Электронная почта уже занята')
            elif not request.POST.get('email') or request.POST.get('email') == " ":
                messages.info(request, 'Заполните поле электронной почта')
            elif not request.POST.get('username') or request.POST.get('username') == " ":
                messages.info(request, 'Заполните поле логин')
            elif not request.POST.get('telephone_number'):
                messages.info(request, 'Заполните поле телефонный номер')
            elif not request.POST.get('password') or request.POST.get('password') == " ":
                messages.info(request, 'Заполните поле пароль')
            elif not request.POST.get('first_name') or request.POST.get('first_name') == " ":
                messages.info(request, 'Заполните поле имя')
            elif not request.POST.get('last_name') or request.POST.get('last_name') == " ":
                messages.info(request, 'Заполните поле фамилия')
            elif not request.POST.get('class_number') or request.POST.get('class_number') == " ":
                messages.info(request, 'Заполните поле номер класса. Вводить нужно только сам номер(цифрой)')
            elif not request.POST.get('name_school') or request.POST.get('name_school') == " ":
                messages.info(request, 'Заполните поле название школы')
            else:
                new_user = User.objects.create_user(username=request.POST.get('username'),
                                               email=request.POST.get('email'), first_name=request.POST.get('first_name'),
                                               last_name=request.POST.get('last_name'), password=request.POST.get('password'))
                user = User.objects.get(username=request.POST.get('username'))
                telephone_number = request.POST.get('telephone_number')
                class_number = request.POST.get('class_number')
                name_school = request.POST.get('name_school')
                class_number_get = ClassNumber.objects.get(name=class_number)
                student = Student.objects.create(user=new_user, telephone_number=telephone_number,
                                                    class_number=class_number_get, name_school=name_school)
                registration_text = "Поздравляем Вас с регистрацией на олимпиаду! \nНиже представлены логин и пароль от Вашего аккаунта. Просим, не сообщать никому данные. \nВаш логин: {0} \nВаш пароль: {1} \nЛюбые возникшие вопросы Вы можете задать в чате технической поддержки на сайте.\nУспешного написания олимпиады!\nС уважением, Школа Точных Наук 'Штерн'!".format(request.POST.get('username'), request.POST.get('password'))
                send_mail(
                    'Регистрация на онлайн олимпиаду',
                    registration_text,
                    settings.EMAIL_HOST_USER,
                    [request.POST.get('email'), ],
                    fail_silently=False
                    )
                
                event_for_user = Event.objects.get(classes__name=class_number_get)
                new_user_in_event = UserInEvent.objects.create(
                                        user=student,
                                        event=event_for_user,
                                        paid=False, active=True, date_registration=datetime.datetime.now())
                if user is not None:
                    auth.login(request, user)
                return redirect('payment')
    return render(request, 'index.html', locals())

def redirect_index(request):
    return redirect('auth_user')

@login_required(login_url='/user/auth/')
def payment(request):
    """

    :param request: standard django param

    **Code**
        account - request username of current user

        desc - description of payment

        sum - dum of payment

        sign_string - collecting the necessary information for signature

        sign - ready-made encrypted signature
    
    :return sign to unitpay server
    """
    student = UserInEvent.objects.get(user__user__username=request.user.username)
    if student.paid == False:
        if request.method == 'POST':
            account = request.user.username
            separator = '{up}'
            params = {
                'account': account,
                'desc': settings.DESC,
                'sum': settings.PRICE,
            }
            sign_string = separator.join(['{}'.format(value) for (key, value) in params.items()])
            sign_string += separator + settings.SECRET_KEY_PAYMENT
            sign = sha256(sign_string.encode('utf-8')).hexdigest()
            params.update({'signature': sign})
            params_string = urlencode(params)
            url = 'https://unitpay.ru/pay/{}?{}'
            return redirect(url.format(settings.MERCHANT_ID, params_string))
    else:
        return redirect(reverse('time_to_start', kwargs={'category_slug': student.event.category.slug, 'slug': student.event.slug}))
    return render(request, 'payment.html', locals())

   
def plus_balls(id, qs, user, txt):
    if Answer.objects.filter(text=txt, question=qs).exists():
        plus = Student.objects.get(user=user)
        if str(id) in settings.DICT_BALLS:
            plus.count += settings.DICT_BALLS(id)
        else:
            plus.count += 1
        plus.save()
    return redirect('tests')

def strftime(date):
    return date.strftime("%Y-%m-%d %H:%M:%S")

@login_required(login_url='/user/auth/')
def time_to_start(request, category_slug, slug):
    time_start = Event.objects.get(slug=slug).data_event
    if datetime.datetime.now().timestamp() < time_start.timestamp():
        return render(request, 'timer.html', {'time_to_start': json.dumps(strftime(time_start))})
    else:
        return redirect(reverse('start_olympiad', kwargs={'category_slug': category_slug, 'slug': slug}))

@login_required(login_url='/user/auth/')
def final(request, category_slug, slug):
    return render(request, 'final.html')

@login_required(login_url='/user/auth/')
def start_olympiad(request, category_slug, slug):
    student = Student.objects.get(user=request.user)
    if student.paid == False:
        return redirect('payment')
    else:
        data = Event.objects.get(slug=slug)
        id_question = Question.objects.filter(event__slug=slug).first()
        if 'start-modal-start' in request.POST:
            return redirect(reverse('question', kwargs={'category_slug': category_slug, 'slug': slug, 'id_question': id_question}))
    return render(request, 'start-olymp.html', locals())

def create_answer(student, txt, qs):
    new = UserAnswer.objects.create(student=student, 
                                    answer=txt,
                                    question=qs)
    new.save()

def time_olymp(user, event):
    student = Student.objects.get(user=user)
    if student.class_number.name in range(1, 3):
        end_time = datetime.datetime.now() + datetime.timedelta(hours=1)
    elif student.class_number.name in range(3, 9):
        end_time = datetime.datetime.now() + datetime.timedelta(hours=1, minutes=30)
    else:
        end_time = datetime.datetime.now() + datetime.timedelta(hours=2)
    if not StartOlymp.objects.filter(user__username=user.username).exists():
        StartOlymp.objects.create(user=user, event=event,
                    start_time=datetime.datetime.now(), end_time=end_time)
    return end_time

@login_required(login_url='/user/auth/')
def question(request, category_slug, slug, id_question):
    questions = Question.objects.filter(event__slug=slug)
    event = Event.objects.get(slug=slug)
    end_olymp_user = time_olymp(user=request.user, event=event)
    return render(request, 'olymp.html', {'end_olymp_user': json.dumps(strftime(end_olymp_user)), "category_slug": category_slug, "slug": slug, "event": event})

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/user/auth/')
def answer(request, id):
    if request.user.student.paid == True:
        question = Question.objects.get(id=id)
        answered_question = UserAnswer.objects.filter(question=question, student=request.user.student).exists()

        if not answered_question:
                            
            if request.method == 'POST': 
        
                form = UserAnswerForm(request.POST)
                if form.is_valid():
                
                    q1 = form.cleaned_data['answer']
                    txt = ''.join(q1)
                    create_answer(request.user.student, txt, question)
                    plus_balls(question.id, question, request.user.student.user, txt)
                    return redirect('tests')
                else:
                    return redirect('tests')
            else:
                form = UserAnswerForm()
        else:
            completed = 'Вы уже ответили на этот вопрос'
        
        return render(request, 'core/answer.html', locals())

    else:
        return redirect('payment')


def signout(request):
    logout(request)
    return redirect('auth_user')

def payment_check(request):
    """
    handler Unitay payment

    :param request: standard django param

    **Code**
        data - data from request UnitPay server

        method - status of payment

        payment - user from db
    
    :return json with message to user
    check this links:
    :https://github.com/unitpay/python-sdk
    :https://github.com/Underlor/unitpay_python_sdk

    """
    data = request.GET.copy()
    method = data.get('method')
		
    if method == 'check':
        try:
            payment = Student.objects.get(user=data.get('params[account]'))
            if payment.paid == True:
                return json.dumps({'message': 'Вы уже оплатили олимпиаду'})
            else:
                return json.dumps({'message': 'Ожидание успешно'})
        except Student.DoesNotExist:
                return json.dumps({'message': 'Неверный обьект обработки. Пользователь не найден'})
    
    elif method == 'pay':
        try:
            payment = Student.objects.get(user=data.get('params[account]'))
            payment.paid = True
            payment.save()
            return json.dumps({'message': 'Оплата успешна'})
        except Student.DoesNotExist:
            return json.dumps({'message': 'Неверный обьект обработки. Пользователь не найден'})
            
    elif method == 'error':
        return json.dumps({'message': 'Произошла какая-то ошибка'})
    
    else:
        return json.dumps({'message': 'Метод не поддерживается'})

@login_required(login_url='/user/auth/')
def bad_payment(request):
    """
    :param request: standard django param

        will be called if the UnitPay server
        response on the board is negative
    """
    return render(request, 'bad-payment.html')


def documents(request):
    return render(request, 'documents.html')

@login_required(login_url='/user/auth/')
def profile(request):
    student = Student.objects.get(user=request.user)
    if request.method == "POST":
        if request.POST.get('class_number') and student.class_number != request.POST.get('class_number'):
            student.class_number = ClassNumber.objects.get(name=request.POST.get('class_number'))
            student.save()
        if request.POST.get('username') and student.user.username != request.POST.get('username'):
            student.user.username = request.POST.get('username')
            student.save()
        if request.POST.get('email') and student.user.email != request.POST.get('email'):
            student.user.email = request.POST.get('email')
            student.save()
        if request.POST.get('telephone_number') and student.telephone_number != request.POST.get('telephone_number'):
            student.telephone_number = request.POST.get('telephone_number')
            student.save()
        if request.POST.get('first_name') and student.user.first_name != request.POST.get('first_name'):
            student.user.first_name = request.POST.get('first_name')
            student.save()
        if request.POST.get('last_name') and student.user.last_name != request.POST.get('last_name'):
            student.user.last_name = request.POST.get('last_name')
            student.save()
        if request.POST.get('name_school') and student.name_school != request.POST.get('name_school'):
            student.name_school = request.POST.get('name_school')
            student.save()
    return render(request, 'profile.html', locals())

@login_required(login_url='/user/auth/')
def succes_payment(request):
    student = Student.objects.get(user__username=request.user.username)
    student_in_event = UserInEvent.objects.get(user=student)
    student_in_event.paid = True
    student_in_event.save()
    event_slug = student_in_event.event.slug
    category_slug = student_in_event.event.category.slug
    return render(request, 'success-payment.html', locals())