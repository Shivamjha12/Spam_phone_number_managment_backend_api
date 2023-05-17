from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
import jwt,datetime
from rest_framework import generics
from .models import *
from Accounts.serializers import *
from GetSpammer import settings
from rest_framework import status

# Create your views here.
class makeSpam(APIView):
    
    def post(self, request):
        
        # token = request.COOKIES.get('jwt')
        # payload = jwt.decode(token,'secret',algorithms=['HS256'])
        # id = User.objects.filter(id=payload['id']).first()

        token = request.COOKIES.get('jwt')
        payload = jwt.decode(token,'secret',algorithms=['HS256'])
        user = User.objects.filter(id=payload['id']).first()
        # query the user if only if user have valid jwt token
        if(User.check_user_exists(user.id)):
                
            phone_number = request.data.get('phone_number')
            user = user

            try:
                spam_number = SpamNumbers.objects.get(phone_number=phone_number)
            except SpamNumbers.DoesNotExist:
                spam_number = SpamNumbers.objects.create(phone_number=phone_number)

            # Mark the number as spam for the user
            spam_number.mark_spam(user)

            return Response({"message": "Number marked as spam."})
        else:
            return Response({
                'response': "please login invalid token"
            }, status=status.HTTP_200_OK)
            
class checkSpam(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        payload = jwt.decode(token,'secret',algorithms=['HS256'])
        user = User.objects.filter(id=payload['id']).first()
        # query the user if only if user have valid jwt token
        if(User.check_user_exists(user.id)):
            phone_number = request.data.get('phone_number')
            user = user
            
            try:
                spam_number = SpamNumbers.objects.get(phone_number=phone_number)
            except SpamNumbers.DoesNotExist:
                return Response({'response':"Number is not a spam number"})
            print(type(spam_number))
            spam = spam_number.spam_count
            print(spam)
            return Response({"message": f'Number may be spam {spam} people marked this number as spam'})
        else:
            return Response({
                'response': "please login invalid token"
            }, status=status.HTTP_200_OK)
            