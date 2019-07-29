from django.db import models
from datetime import datetime

class Contact(models.Model):
    user_id = models.IntegerField()
    listing_id = models.IntegerField()
    address=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name