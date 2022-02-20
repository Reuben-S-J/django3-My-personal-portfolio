from django.db import models

# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    image= models.ImageField(upload_to='portfolio/images/')
    url=models.URLField(blank=True)
    file=models.FileField(upload_to='portfolio/files/',blank=True)

    def __str__(self):#to add title to the model name instead of project 1,2 etc...
        return self.title
