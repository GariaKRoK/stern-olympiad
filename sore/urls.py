from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('', redirect_index),
    path('user/signup', signup, name='signup'),
    path('user/signin', signin, name='signin'),
    path('payment/', payment, name='payment'),
    path('bad-payment/', bad_payment, name='bad_payment'),
    path('succes-payment/', succes_payment, name='succes_payment'),
    path('payment-check/', payment_check),
    path('olymp/', olymp, name='olymp'),
    path('tests/', tests, name='tests'),
    path('index/', index, name='index'),
    re_path('(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/(?P<id>[\w-]+)$', question, name='question'), 
    re_path('(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/final/', final, name='final'),
    re_path('(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/time-to-start/', time_to_start, name='time_to_start'),
    re_path('(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)', start_olympiad, name='start_olympiad'),
    path('completed/', completed, name='completed'),
    path('timeout/', timeout, name='timeout'),
    path('profile/', profile, name='profile'),
    path('documents/', documents, name='documents'),
]