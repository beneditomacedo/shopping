""" api """
from rest_framework import viewsets
from shopping.models import Retailer
from .serializers import RetailerSerializer

class RetailerViewSet(viewsets.ModelViewSet):
    """ api Retailter """
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer
