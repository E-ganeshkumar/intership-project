from django.shortcuts import render
from rest_framework import generics
from .models import userlogin
from .serializers import serializeruser

class creatgetapi(generics.ListCreateAPIView):
    queryset = userlogin.objects.all()
    serializer_class = serializeruser

class updatedeletegetidapi(generics.RetrieveUpdateDestroyAPIView):
    queryset = userlogin.objects.all()
    serializer_class = serializeruser
