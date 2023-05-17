from django.urls import path, include
from .views import *

urlpatterns = [
    path('addspam',makeSpam.as_view()),
    path('checkspam',checkSpam.as_view()),
]