from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.surname}"

