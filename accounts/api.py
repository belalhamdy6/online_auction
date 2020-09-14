from rest_framework import generics
from .Serializers import ProfileApi, UserApi
from .forms import *


class Profile_Api(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileApi

class User_Api(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserApi

