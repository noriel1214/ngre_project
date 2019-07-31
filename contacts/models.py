from django.db import models
from datetime import datetime

class Contact(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.firstname + " " + self.lastname