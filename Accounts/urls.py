from django.urls import path, include
from .views import *

urlpatterns = [
    path('register', register.as_view()),
    path('login', login.as_view()),
    path('user', userView.as_view()),
    path('logout', logout.as_view()),
    
]