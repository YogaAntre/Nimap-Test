from django.contrib import admin
from .models import User_p,Project1



class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(User_p,UserAdmin)

class Project1Admin(admin.ModelAdmin):
    list_display = ['id','project_name','clients','user','created_at','created_by']
admin.site.register(Project1,Project1Admin)
