from django.db import models

class user(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mail = models.EmailField(unique=True)
    birthday = models.DateField()
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.name} {self.lastname}"