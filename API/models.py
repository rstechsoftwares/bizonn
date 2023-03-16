from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    productID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    productImg = models.ImageField(upload_to='accounts/images')
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Category(models.Model):
    categoryID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoryName = models.CharField(max_length=50)
    product = models.ForeignKey('Product', related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.categoryName

class Retailer(models.Model):
    retailerID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    phoneNumber = models.BigIntegerField(blank=False, unique=True)
    category = models.ForeignKey('Category', related_name='categoryRetailer', on_delete=models.CASCADE)
    gstNo = models.CharField(max_length=50)
    shopName = models.CharField(max_length=50, blank=False)
    tradeLicence = models.CharField(max_length=50, blank=False)
    shopPhoneNumber = models.BigIntegerField(blank=False)
    shopImg = models.ImageField(upload_to='accounts/images', blank=False)
    shopAddress = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()

    def __str__(self):
        return self.shopName


class Manufacturer(models.Model):
    manufacturerID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=30, blank=False)
    phoneNumber = models.BigIntegerField(blank=False, unique=True)
    category = models.ForeignKey('Category', related_name='categoryManufacturer', on_delete=models.CASCADE)
    gstNo = models.CharField(max_length=50)
    companyName = models.CharField(max_length=50, blank=False)
    companyPhoneNUmber = models.BigIntegerField(blank=False)
    companyLogo = models.ImageField(upload_to='accounts/images', blank=False)
    companyAddress = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()

    def __str__(self):
        return self.companyName

class Wholeseller(models.Model):
    wholesellerID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=30, blank=False)
    phoneNumber = models.BigIntegerField(blank=False, unique=True)
    category = models.ForeignKey('Category', related_name='categoryWholeseller', on_delete=models.CASCADE)
    gstNo = models.CharField(max_length=50)
    distributerName = models.CharField(max_length=50, blank=False)
    distributerPhoneNUmber = models.BigIntegerField(blank=False)
    distributerLogo = models.ImageField(upload_to='accounts/images', blank=False)
    distributerAddress = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()

    def __str__(self):
        return self.distributerName