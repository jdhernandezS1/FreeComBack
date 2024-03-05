from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


class UserInfo(models.Model):
    USER_TYPE_CHOICES = [
        ('client', 'Client'),
        ('seller', 'Seller'),
        ('small_business', 'Small Business'),
        ('large_business', 'Large Business'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='client')
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    post_code = models.CharField(max_length=10, blank=True, null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    birth_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    surName = models.CharField(max_length=50, blank=True, null=True)
    # servicios_favoritos = models.ManyToManyField('Servicio', related_name='usuarios_favoritos', blank=True)


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields for company-specific information


class SmallBusiness(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    product_category = models.CharField(max_length=50)
    # Other fields specific to small businesses


class LargeBusiness(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    # Additional fields for large businesses


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Other fields for products


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Other fields for services


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Other fields specific to individual sellers


class Sale(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    products_sold = models.ManyToManyField(Product)
    services_sold = models.ManyToManyField(Service)
    # Other fields as needed
