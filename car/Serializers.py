from .models import *
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'




class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid_price
        fields = '__all__'