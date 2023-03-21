from django.db import models


class Organisation(models.Model):
    ORG_CHOICES = [
        ("ORG1", "ORG1"),
        ("ORG2", "ORG2"),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=4, choices=ORG_CHOICES)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Organisation(id={self.id}, name='{self.name}', type='{self.type}', location='{self.location}')"


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email_address = models.EmailField(null=True, blank=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.surname}"

    def __repr__(self):
        return f"Person(id={self.id}, first_name='{self.first_name}', surname='{self.surname}', email_address='{self.email_address}', organisation_id={self.organisation_id})"
