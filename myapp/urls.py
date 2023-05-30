from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('registration/', user_registration, name='registration'),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('note/', NoteView.as_view(), name='note'),
]
