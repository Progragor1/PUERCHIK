from django.urls import path
from .views import *

urlpatterns=[
    path('', index, name='index'),
    path('marina/', women),
    path('test/',test, name='test'),
    path('add_note/',add_note, name = 'add_note')

]