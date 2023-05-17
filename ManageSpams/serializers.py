from rest_framework import serializers
from .models import *
from Accounts.serializers import *

class SpamNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamNumbers
        fields = ['phone_number']