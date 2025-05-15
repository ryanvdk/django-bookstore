from django.db import models

# Create your models here.


class Book(models.Model):
    # char field type max_length is required, ID column is automatically created.
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
