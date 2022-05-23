from django.shortcuts import render
from .models import Clients,Projects,User_p,Project1
from .serializers import ProjectsSerializer,ClientsSerializer,UserSerializer,Project1Serializer
from rest_framework import generics


# Create your views here.
class Clients_info(generics.ListCreateAPIView):
    #queryset = Clients.objects.select_related('projects__name','projects__clients')
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

class Clients_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
class Projects_info(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class User_details(generics.ListCreateAPIView):
    queryset = User_p.objects.all()
    serializer_class = UserSerializer

class Projects1_info(generics.ListCreateAPIView):
    queryset = Project1.objects.all()
    serializer_class = Project1Serializer




