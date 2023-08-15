from django.db import models

class Instrument(models.Model):
    type = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    inStock = models.BooleanField()
    def __str__(self): 
        return f"{self.model}"

class Client(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=20) 
    def __str__(self):
        return f"{self.name}"

class Branch(models.Model):
    name = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
