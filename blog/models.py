from django.db import models

class Blog(models.Model):
    title= models.CharField(max_length=100)
    Date=models.DateTimeField(auto_now=False, auto_now_add=False)
    description=models.CharField(max_length=200000)

    def __str__(self):#to add title to the model name instead of project 1,2 etc...
        return self.title
