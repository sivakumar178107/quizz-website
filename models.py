from django.db import models

# Create your models here.
class exam(models.Model):
    question=models.CharField(max_length=250)
    option1=models.CharField(max_length=250)
    option2=models.CharField(max_length=250)
    option3=models.CharField(max_length=250)
    option4=models.CharField(max_length=250)
    corrans=models.CharField(max_length=250)


