from rest_framework import serializers
from django.conf import settings
from django.contrib import auth

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = auth.get_user_model()
        fields = ('id',
                  'username',)