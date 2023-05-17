from rest_framework import serializers
from .models import *
from Accounts.serializers import *
class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['name', 'phone_number']
        
        
    def create(self,validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
    
    def validate(self, data):
        request = self.context.get('request')
        user = request.user if request else None
        phone_number = data['phone_number']

        # Here we Checking if a contact with the same phone number already exists for the user
        if Contacts.objects.filter(user=user, phone_number=phone_number).exists():
            raise serializers.ValidationError("Contact with this phone number already exists.")

        return data



class ContactNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['name','phone_number']

class UserNameSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        # Access the model instance and call the property method
        return obj.full_name
    class Meta:
        model = User
        fields = ['name','phone']

# class SearchNameSerializer(serializers.Serializer):
#     contacts = ContactNameSerializer(many=True)
#     # users = UserNameSerializer(many=True)
#     users = serializers.SerializerMethodField()

#     def get_users(self, obj):
#         # Convert User objects to dictionary representation
#         users_data = UserNameSerializer(obj['users'], many=True).data
#         return users_data