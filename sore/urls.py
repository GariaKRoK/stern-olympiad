from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('', redirect_index),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('payment/', payment, name='payment'),
    path('failed-payment/', failed_payment, name='failed_payment'),
    path('payment-check/', payment_check),
    path('olymp/', olymp, name='olymp'),
    path('tests/', tests, name='tests'),
    re_path('(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/time-to-start/', time_to_start, name='time_to_start'),
    path('completed/', completed, name='completed'),
    path('timeout/', timeout, name='timeout'),
    path('contacts/', contacts, name='contacts'),
    path('agreement/', agreement, name='agreement'),
    path('description/', description, name='description'),
    path('confidentiality/', confidentiality, name='confidentiality'),
    re_path('tests/(?P<id>[\w-]+)$', answer, name='answer')
]