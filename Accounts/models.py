from django.db import models
from django.contrib.auth.models import AbstractUser
from Accounts.managers import CustomUserManager
from django.core.validators import RegexValidator

class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone = models.CharField(max_length=20, validators=[phone_regex], blank = False, null=False,unique = True)
    email = models.EmailField(max_length=255,blank = True, null=True)
    password = models.CharField(max_length=255)
    username = None
    
    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=[]
    objects = CustomUserManager()
    
    def __str__(self):
        return  self.first_name + " " + self.last_name 

    # @property
    # def token(self):
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
    @classmethod
    def check_user_exists(self,user_id):
        return User.objects.filter(id=user_id).exists()
        

    
