from django.db import models
from Accounts.models import User

# Create your models here.
class SpamNumbers(models.Model):
    phone_number = models.CharField(max_length=20,validators=[User.phone_regex],unique=True)
    users = models.ManyToManyField(User, related_name='spam_numbers')

    def mark_spam(self, user):
        self.users.add(user)

    def unmark_spam(self, user):
        self.users.remove(user)

    @property
    def spam_count(self):
        return self.users.count()
    
    def __str__(self):
        return "The spam count of phone number "+ self.phone_number +" is "+ str(self.spam_count)