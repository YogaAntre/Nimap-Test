from django.db import models

# Create your models here.
class Clients(models.Model):
    client_name =models.CharField(max_length=50)
    created_at =models.DateTimeField()
    created_by = models.CharField(max_length=50)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.client_name

class Projects(models.Model):
    name = models.CharField(max_length=100)
    clients = models.ForeignKey(Clients,on_delete=models.CASCADE,related_name='projects')

    def __str__(self):
        return self.name
class User_p(models.Model):

    name = models.CharField(max_length=100)
    #user = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='user')
    def __str__(self):
        return self.name

class Project1(models.Model):
    project_name=models.CharField(max_length=100)
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='projects1')
    user = models.ForeignKey(User_p, on_delete=models.CASCADE, related_name='user1')
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=50)

    def __str__(self):
        return self.project_name


