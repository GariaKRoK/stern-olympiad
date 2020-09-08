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
from datetime import datetime
def signin(request):
    """
        signin view
        using django authenticate mechanism
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('payment')
        else:
            return redirect('signin')
    else:
        return render(request, 'user/signin.html')
    return render(request, 'user/signin.html')

def redirect_index(request):
    return redirect('signin')

def signup(request):
    
    """
    signup view

        user_form - form for registration user
        
        student_form - form for registration student

        send_email - send mail to user mail about his signup
        
        using django authenticate mechanism
    """
    if request.method == 'POST':
        user_form = SignUpUserForm(request.POST)
        student_form = SignUpStudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
                
            if User.objects.filter(email=user_form.cleaned_data.get('email')).exists():
                messages.info(request, 'Электронная почта уже занята')
                user_form = SignUpUserForm()
                student_form = SignUpStudentForm()
            else:

                user = user_form.save(commit=False)
                email = user_form.cleaned_data.get('email')

                user_form.save()

                login(request, user, backend='django.contrib.auth.backends.ModelBackend')            
                student = student_form.save(commit=False) 
                student.user = User.objects.get(username=user_form.cleaned_data.get('username'))
                student.telephone_number = student_form.cleaned_data.get('telephone_number')
                student.class_number = student_form.cleaned_data.get('class_number')
                student.name_school = student_form.cleaned_data.get('name_school')
                student_form.save()

                with open('send.txt', 'r+', encoding='UTF-8') as f:
                    old_file_content = f.read() # read everything in the file
                    
                    #insert data into txt file
                    new_file_content = old_file_content.format(
                                                str(user_form.cleaned_data.get('username')),
                                                str(user_form.cleaned_data.get('password1')))
                    
                    #send mail with password and username to new user
                    send_mail(
                        'Регистрация на онлайн олимпиаду',
                        str(new_file_content),
                        settings.EMAIL_HOST_USER,
                        [email, ],
                        fail_silently=False
                        )
                
                return redirect('payment')
                
        else:
            if User.objects.filter(username=request.POST.get('username')).exists():
                messages.info(request, 'Логин уже занят')
                user_form = SignUpUserForm()
                student_form = SignUpStudentForm()
            else:
                messages.info(request, 'Пароли не совпадают или пароль меньше 8 символов')
                user_form = SignUpUserForm()
                student_form = SignUpStudentForm()
            
    else:
        user_form = SignUpUserForm()
        student_form = SignUpStudentForm()

    return render(request, 'user/signup.html', locals())


@login_required(login_url='/signin/')
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
    if request.method == 'POST':
        #if request.user.student.paid:
        #    return redirect('olymp')
        #else:
        account = request.user.username
        separator = '{up}'
        params = {
            'account': account,
            'desc': settings.DESC,
            'sum': settings.PRICE,
        }
        sign_string = separator.join(['{}'.format(value) for (key, value) in params.items()])
        sign_string += separator + settings.SECRET_KEY
        sign = sha256(sign_string.encode('utf-8')).hexdigest()
        params.update({'signature': sign})
        params_string = urlencode(params)
        url = 'https://unitpay.ru/pay/{}?{}'
        return redirect(url.format(settings.MERCHANT_ID, params_string))
    return render(request, 'payment.html', locals())



@login_required(login_url='/signin/')
def tests(request):
    """
    tests view
    
    :param request: standard django param

    **Code**
        class_number - class number of user

        link_timer - timer of user olympiad

        question - all questions for user
    """
    if request.user.student.paid == True:
        class_number = request.user.student.class_number
        link_timer = settings.DICT_LINK_TIMER[str(class_number)]
        question = Question.objects.filter(class_number=request.user.student.class_number)
        
        return render(request, 'core/tests.html', {'question': question, 'link_timer': link_timer})
    else:
        return redirect('payment')
        
def plus_balls(id, qs, user, txt):
    if Answer.objects.filter(text=txt, question=qs).exists():
        plus = Student.objects.get(user=user)
        if str(id) in settings.DICT_BALLS:
            plus.count += settings.DICT_BALLS(id)
        else:
            plus.count += 1
        plus.save()
    return redirect('tests')


def time_to_unix(date):
    return datetime.strptime(date, '%Y-%b-%d %I:%M')

@login_required(login_url='/signin/')
def time_to_start(request, category_slug, slug):
    time_start = Event.objects.get(slug=slug).data_event
    time_start_str = time_start.strftime("%Y-%m-%d %H:%M:%S")
    #if time_to_unix(datetime.now()) > time_to_unix(time_start):
    return render(request, 'timer.html', {'time_to_start': json.dumps(time_start_str)})
    #else:
    #    return redirect('olympiad', kwargs={'category_slug': category_slug, 'slug': slug})

@login_required(login_url='/signin/')
def final(request, category_slug, slug):
    return render(request, 'final.html')

@login_required(login_url='/signin/') 
def start_olympiad(request, category_slug, slug):
    data = Event.objects.get(slug=slug)
    return render(request, 'start-olymp.html', locals())

def create_answer(student, txt, qs):
    new = UserAnswer.objects.create(student=student, 
                                    answer=txt,
                                    question=qs)
    new.save()


@login_required(login_url='/signin/')
def question(request, category_slug, slug, id):
    return render(request, 'olymp.html')

@login_required(login_url='/signin/')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/signin/')
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


@login_required(login_url='/signin/')
def olymp(request):
    """
        if user visit this url,
        then he paid for olympiad :)
    """
    qs = Student.objects.get(user=request.user.student.user)
    qs.paid = True
    qs.save()
    return render(request, 'core/olymp.html')


@login_required(login_url='/signin/')
def completed(request):
    #will be called if user completed olympiad
    return render(request, 'info/completed.html')

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

@login_required(login_url='/signin/')
def bad_payment(request):
    """
    :param request: standard django param

        will be called if the UnitPay server
        response on the board is negative
    """
    return render(request, 'bad-payment.html')

@login_required(login_url='/signin/')
def timeout(request):
    #will be called if the time of your olympiad is over
    return render(request, 'info/timeout.html')

      
def description(request):
    return render(request, 'info/description.html')  

@login_required(login_url='/signin/')   
def documents(request):
    return render(request, 'documents.html')

@login_required(login_url='/signin/')   
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/signin/')   
def succes_payment(request):
    return render(request, 'success-payment.html')