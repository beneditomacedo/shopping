from shopping.models import Retailer
from rest_framework import serializers

class RetailerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Retailer
        fields = [ 'name' ]