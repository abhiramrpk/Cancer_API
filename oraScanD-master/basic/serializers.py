from rest_framework import serializers
from .models import MyModel, Print

class MyModelSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source='creator.username')
    creator_id = serializers.ReadOnlyField(source='creator.id')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = MyModel
        fields = ['id', 'creator', 'creator_id', 'title', 'description', 'image_url']

class PrintSerializer(serializers.ModelSerializer):

    image_url = serializers.ImageField(required=True)

    class Meta:
        model = Print
        fields = ['id','image_url']