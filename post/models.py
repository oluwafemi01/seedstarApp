from django.db import models

# Create your models here.
class post(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)  
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    
    def __str__(self):
        return self.firstname

    class Meta:
        ordering = ["-updated"]
    

                                
