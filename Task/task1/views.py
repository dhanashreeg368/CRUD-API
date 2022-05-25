from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from task1.serializers import task1Serializer
from task1.models import task1

# Create your views here.

class Listtask1APIView(ListAPIView):
    """This endpoint list all of the available fields from the database"""
    queryset = task1.objects.all()
    serializer_class = task1Serializer

class Createtask1APIView(CreateAPIView):
    """This endpoint allows for creation of a task1"""
    queryset = task1.objects.all()
    serializer_class = task1Serializer

class Updatetask1APIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the task1 to update"""
    queryset = task1.objects.all()
    serializer_class = task1Serializer

class Deletetask1APIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific task1 from the database"""
    queryset = task1.objects.all()
    serializer_class = task1Serializer



