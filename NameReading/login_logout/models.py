from django.db import models

# Create your models here.
class singup_model(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
