from rest_framework import serializers
from .models import MyModel, Print


class PrintSerializer(serializers.ModelSerializer):

    image_url = serializers.ImageField(required=True)

    class Meta:
        model = Print
        fields = ['id','image_url']

class MyModelSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.IntegerField()
    height = serializers.IntegerField()
    blood_group = serializers.CharField()
    profile_url = serializers.ImageField()

    class Meta:
        model = MyModel
        fields = ['id', 'name', 'age', 'weight', 'height', 'blood_group', 'profile_url', 'image_url']
