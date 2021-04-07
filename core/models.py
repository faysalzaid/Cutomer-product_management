from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,blank=True,null=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    slug = models.SlugField(blank=True,null=True,unique=True)
    phone = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if  self.name:
            slug_gen= str(slugify(self.name))
        else:
            slug_gen = str(slugify(self.user.username))

        self.slug = slug_gen
        return super().save(*args, **kwargs)


class Product(models.Model):
    CATEGORY =(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )
    name= models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100,choices=CATEGORY)
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag')


    def __str__(self):
        return self.name
    


class Tag(models.Model):
    name = models.CharField(max_length=50)\

    def __str__(self):
        return self.name
    

class Order(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('Out for delivery','Out for delivery')
    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,null=True,on_delete=models.CASCADE)
    date_created= models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,choices=STATUS)
    slug = models.SlugField(blank=True,null=True)

    def __str__(self):
        return f"{self.customer.name} ({self.product.name})"
    

    def save(self,*args, **kwargs):
        if self.customer.name:
            slug_= str(slugify(self.customer.name))
        self.slug = slug_ 
        return super().save(*args, **kwargs)