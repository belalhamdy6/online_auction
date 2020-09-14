from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class ProfileApi(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserApi(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


