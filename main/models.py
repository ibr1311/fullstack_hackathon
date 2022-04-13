from django.db import models

# Create your models here.
class Type(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='products')
    model = models.CharField(max_length=255)
    charac = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)



    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ImageField(upload_to='img', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')