from django.contrib import admin
from . models import Request

myModels = [Request] 
admin.site.register(myModels)
