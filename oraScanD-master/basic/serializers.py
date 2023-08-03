from rest_framework import serializers
from .models import MyModel, Print

class MyModelSerializer(serializers.ModelSerializer):
    
    name = serializers.ReadOnlyField()
    age = serializers.ReadOnlyField()
    weight = serializers.ReadOnlyField()
    height = serializers.ReadOnlyField()
    blood_group = serializers.ReadOnlyField()
    image_url = serializers.ImageField()

    class Meta:
        model = MyModel
        fields = ['id', 'name', 'age', 'weight', 'height', 'blood_group', 'image_url']

class PrintSerializer(serializers.ModelSerializer):

    image_url = serializers.ImageField(required=True)

    class Meta:
        model = Print
        fields = ['id','image_url']