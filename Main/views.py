from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from .serializers import *
import jwt,datetime
from rest_framework import generics
from .models import *
from Accounts.serializers import *
from GetSpammer import settings
from rest_framework import status
class ContactsView(APIView):
    
    
    def post(self,request):
        token = request.COOKIES.get('jwt')
        payload = jwt.decode(token,'secret',algorithms=['HS256'])
        user = User.objects.filter(id=payload['id']).first()
        # query the user if only if user have valid jwt token
        if(User.check_user_exists(user.id)):
            serializers = ContactsSerializer(data=request.data,context={'request': request})
            serializers.is_valid(raise_exception=True)
            serializers.save(user=request.user)
            return Response(serializers.data)
        
        else:
            return Response({
                'response': "please login invalid token"
            }, status=status.HTTP_200_OK)

class getContactsView(APIView):
    
    
    
    def get(self, request):
        user = request.user
        contacts = Contacts.get_contacts(user)
        serializer = ContactsSerializer(contacts, many=True)
        return Response(serializer.data)

    
class searchbyname(APIView):
    def post(self, request):
        search_query = request.data.get('search_query', '')
        
        contacts_results = Contacts.objects.filter(name__icontains=search_query)
        users_results = User.objects.filter(first_name__icontains=search_query)
        contacts_serializer = ContactNameSerializer(contacts_results, many=True)
        users_serializer = UserNameSerializer(users_results, many=True)

        # Validate and return the serialized results
        results = []
        results.extend(contacts_serializer.data)
        results.extend(users_serializer.data)

        return Response({
            'results': results
        }, status=status.HTTP_200_OK)

class searchbyname(APIView):
    def post(self, request):
        search_query = request.data.get('search_query', '')
        
        token = request.COOKIES.get('jwt')
        payload = jwt.decode(token,'secret',algorithms=['HS256'])
        user = User.objects.filter(id=payload['id']).first()
        # query the user if only if user have valid jwt token
        if(User.check_user_exists(user.id)):
            contacts_results = Contacts.objects.filter(name__icontains=search_query)
            users_results = User.objects.filter(first_name__icontains=search_query)
            contacts_serializer = ContactNameSerializer(contacts_results, many=True)
            users_serializer = UserNameSerializer(users_results, many=True)

            # Validate and return the serialized results
            results = []
            results.extend(contacts_serializer.data)
            results.extend(users_serializer.data)

            return Response({
                'results': results
            }, status=status.HTTP_200_OK)
            
        else:
            return Response({
                'response': "please login invalid token"
            }, status=status.HTTP_200_OK)
            
            
class searchbyphone(APIView):
    def post(self, request):
        search_query = request.data.get('search_query', '')
        
        token = request.COOKIES.get('jwt')
        payload = jwt.decode(token,'secret',algorithms=['HS256'])
        user = User.objects.filter(id=payload['id']).first()
        # query the user if only if user have valid jwt token
        if(User.check_user_exists(user.id)):
            contacts_results = Contacts.objects.filter(phone_number__icontains=search_query)
            users_results = User.objects.filter(phone__icontains=search_query)
            contacts_serializer = ContactNameSerializer(contacts_results, many=True)
            users_serializer = UserNameSerializer(users_results, many=True)

            # Validate and return the serialized results
            results = []
            results.extend(contacts_serializer.data)
            results.extend(users_serializer.data)

            return Response({
                'results': results
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'response': "please login invalid token"
            }, status=status.HTTP_200_OK)