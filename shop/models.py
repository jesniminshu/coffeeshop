from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to="pictures/")
    description = models.TextField()
    slug = models.SlugField(max_length=100,unique=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Auto-generate slug from name if not provided
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to="pictures/")
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name