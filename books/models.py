from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    condition = models.IntegerField()  # Rating between 1-5
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    isrented = models.BooleanField(default=False)

    def __str__(self):
        return self.name