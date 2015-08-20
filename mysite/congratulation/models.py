from django.db import models
from django.utils import timezone

class Customer(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    user_id = models.IntegerField(null=True)
    def __str__(self):
        return self.last_name

class Details(models.Model):
    customer = models.ForeignKey(Customer)
    text = models.CharField(max_length=300)
    location = models.CharField(max_length=25)
    date = models.DateTimeField('date')
    comment = models.TextField(null=True)
    def __str__(self):
        return self.text