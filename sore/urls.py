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
    path('completed/', completed, name='completed'),
    path('timeout/', timeout, name='timeout'),
    path('contacts/', contacts, name='contacts'),
    path('agreement/', agreement, name='agreement'),
    path('description/', description, name='description'),
    path('confidentiality/', confidentiality, name='confidentiality'),
    path('tests/32', answer32, name='answer32'),
    path('tests/38', answer38, name='answer38'),
    path('tests/23', answer23, name='answer23'),
    path('tests/68', answer68, name='answer68'),
    path('tests/48', answer48, name='answer48'),
    path('tests/29', answer29, name='answer29'),
    path('tests/45', answer45, name='answer45'),
    re_path('tests/(?P<id>[\w-]+)$', answer, name='answer')
]