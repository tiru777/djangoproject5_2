from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField()
    address = models.TextField()
    dob = models.DateField(blank=True,null=True)
    age = models.IntegerField()
    photo = models.FileField(blank=True,null=True)

    def __str__(self):
        return self.first_name
