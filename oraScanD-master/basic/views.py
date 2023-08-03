from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse
from .models import MyModel, Print
from .serializers import MyModelSerializer,PrintSerializer
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .ml import load_Model
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token


import logging

# class MyModelViewSet(viewsets.ModelViewSet):
#     queryset = MyModel.objects.all()#.order_by('-creation_date')
#     serializer_class = MyModelSerializer
#     parser_classes = (MultiPartParser, FormParser)
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(creator=self.request.user)


@api_view(['GET'])
def api_views(request):
    api_urls = {
        'list':'/list/',
        'upload': '/upload/',
    }
    return Response(api_urls)

@api_view(['GET'])
def list(request):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer(queryset,many=True)
    return JsonResponse(serializer_class.data, safe=False)

@api_view(['GET'])
def print(request):
    queryset = Print.objects.all()
    serializer_class = PrintSerializer(queryset,many=True)
    return JsonResponse(serializer_class.data, safe=False)

@api_view(['POST'])
@parser_classes((MultiPartParser, FormParser))
def upload(request):
    serializer_class = PrintSerializer(data=request.data)
    if serializer_class.is_valid():
        #image_data = serializer_class.validated_data['image_url']
        serializer_class.save()
        accuracy = load_Model()
        return HttpResponse(accuracy[0])
        
    else:
        return Response(serializer_class.errors)
 

def get_csrf_token(request):
    # Get the CSRF token from the request's cookies
    csrf_token = get_token(request)

    # Return the CSRF token as a JSON response
    return JsonResponse({'csrf_token': csrf_token})