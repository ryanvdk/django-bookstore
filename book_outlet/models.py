from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=8)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.postal_code}"
    # Let's you control meta data for your model and configure behaviours of your model. Nested Meta Class used to register special settings

    class Meta:
        # Singular form verbose_name = "Address"
        verbose_name_plural = "Addresses"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Book(models.Model):
    # char field type max_length is required, ID column is automatically created.
    title = models.CharField(max_length=50)
    # rating = models.IntegerField(
    #          validators=[MinValueValidator(1), MaxLengthValidator(5)])
    rating = models.IntegerField()
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")
    published_countries = models.ManyToManyField(
        Country, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",
                            null=False, db_index=True)

    # Overrides how the object is represented when the string method is called, so for example how it is displayed in the console.
    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("book_details", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
