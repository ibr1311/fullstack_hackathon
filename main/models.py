from django.db import models

# Create your models here.
from account.models import User


class Type(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='products')
    model = models.CharField(max_length=255)
    charac = models.CharField(max_length=255)
    titles = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='img', blank=True, null=True)



    def __str__(self):
        return self.titles


class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comment', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s - %s' % (self.product.model, self.name)

class ProductLikes(models.Model):
    likeusers = models.ManyToManyField(User)
    likeproduct = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='like')