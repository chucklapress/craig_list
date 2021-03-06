from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class Listing(models.Model):
    category = models.CharField(max_length=30)
    shopper = models.CharField(max_length=30)
    item_price = models.IntegerField()

    # image = models.ImageField(upload_to="image_photos", null=True, verbose_name='image_photos', blank= True)
    def __str__(self):
        return self.shopper

class Category(models.Model):
    name = models.CharField(max_length=30)
    item_location = models.CharField(max_length=20)
    post_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class meta:
        ordering = ["-created"]

class SubCategory(models.Model):
    name = models.ForeignKey(Category)
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


class Region(models.Model):
    location = models.CharField(max_length=30)
    location_name = models.ForeignKey(Category)

    def __str__(self):
        return self.location

@receiver(post_save, sender="auth.User")
def create_token(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Token.objects.create(user=instance)
