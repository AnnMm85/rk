from django.contrib.auth.models import AbstractUser
from django.db import models


class CustUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', blank=True)


class Product(models.Model):
    name = models.CharField(max_length=60)
    desc = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='product_photo/')


class Basket(models.Model):
    user = models.ForeignKey(CustUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_d = models.DateTimeField(auto_now_add=True)
