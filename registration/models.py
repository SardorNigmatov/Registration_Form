from django.db import models

# Create your models here.

class RegistrationModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    company = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    area_code = models.CharField(max_length=5)
    exist = models.CharField(max_length=2)

    class Meta:
        db_table = 'registration'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"