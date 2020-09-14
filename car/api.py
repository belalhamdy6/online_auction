from rest_framework import generics
from .models import Job, Bid_price
from .Serializers import JobSerializer, BidSerializer


class CarListApi(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    lookup_field = 'id'


class Bid_Detail(generics.ListCreateAPIView):
    queryset = Bid_price.objects.all()
    serializer_class = BidSerializer
