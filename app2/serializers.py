from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Category_view(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'    