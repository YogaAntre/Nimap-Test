from .models import Projects,Clients,User_p,Project1
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_p
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    user= UserSerializer(read_only=True,many=True)

    class Meta:
        model = Projects

        fields = '__all__'

class ClientsSerializer(serializers.ModelSerializer):
    projects = ProjectsSerializer(read_only=True,many=True)
    class Meta:
        model = Clients

        fields = '__all__'




class Project1Serializer(serializers.ModelSerializer):
    projects1 = ClientsSerializer(read_only=True, many=True)
    user1 = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Project1
        fields = '__all__'

