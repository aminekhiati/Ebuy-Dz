from django.db import models
from django.conf import settings

# Create your models here.

Category = (
    ('shirt','Shirt'),
    ('pants','Pants'),
    ('jacket','Jacket')
)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    d_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=Category,default='shirt', max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class ProductToCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Cart (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductToCart)
    date = models.DateField(auto_now_add=True)
    