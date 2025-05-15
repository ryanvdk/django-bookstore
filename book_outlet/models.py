from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    # char field type max_length is required, ID column is automatically created.
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxLengthValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    # Overrides how the object is represented when the string method is called, so for example how it is displayed in the console.
    def __str__(self):
        return f"{self.title}{" by " + self.author if self.author else ""} ({self.rating}) {"Best Seller" if self.is_bestselling else ""}"

    def get_absolute_url(self):
        return reverse("book_details", args=[self.pk])
