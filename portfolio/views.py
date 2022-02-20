from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.
def home (request):
    projects=Project.objects.all()#grabs all the objects from the data base
    return render (request,'portfolio\home.html',{'projects':projects})
