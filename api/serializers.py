""" serializers """
from rest_framework import serializers
from shopping.models import Retailer

class RetailerSerializer(serializers.HyperlinkedModelSerializer):
    """ Retailer serializer """
    class Meta:
        model = Retailer
        fields = ['name', 'url']
