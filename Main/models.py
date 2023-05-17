from django.db import models
from Accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.core.validators import RegexValidator
# phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")

class Contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20,validators=[User.phone_regex])
    
    class Meta:
        unique_together = ('phone_number', 'user')
    
    @classmethod
    def get_contacts(cls, user):
        contacts = cls.objects.filter(user=user)
        return contacts



    