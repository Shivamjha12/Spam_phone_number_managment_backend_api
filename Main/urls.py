from django.urls import path, include
from .views import *

urlpatterns = [
    path('addcontact', ContactsView.as_view()),
    path('getcontact', getContactsView.as_view()),
    path('searchbyname', searchbyname.as_view()),
    path('searchbyphonenumber', searchbyphone.as_view()),
]