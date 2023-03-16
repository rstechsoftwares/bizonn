# Generated by Django 4.1.7 on 2023-03-09 21:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='API.product')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('manufacturerID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('phoneNumber', models.BigIntegerField(unique=True)),
                ('gstNo', models.CharField(max_length=50)),
                ('companyName', models.CharField(max_length=50)),
                ('companyPhoneNUmber', models.BigIntegerField()),
                ('companyLogo', models.ImageField(upload_to='accounts/images')),
                ('companyAddress', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryManufacturer', to='API.category')),
            ],
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('retailerID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('phoneNumber', models.BigIntegerField(unique=True)),
                ('gstNo', models.CharField(max_length=50)),
                ('shopName', models.CharField(max_length=50)),
                ('tradeLicence', models.CharField(max_length=50)),
                ('shopPhoneNumber', models.BigIntegerField()),
                ('shopImg', models.ImageField(upload_to='accounts/images')),
                ('shopAddress', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryRetailer', to='API.category')),
            ],
        ),
        migrations.CreateModel(
            name='Wholeseller',
            fields=[
                ('wholesellerID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('phoneNumber', models.BigIntegerField(unique=True)),
                ('gstNo', models.CharField(max_length=50)),
                ('distributerName', models.CharField(max_length=50)),
                ('distributerPhoneNUmber', models.BigIntegerField()),
                ('distributerLogo', models.ImageField(upload_to='accounts/images')),
                ('distributerAddress', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryWholeseller', to='API.category')),
            ],
        ),
        migrations.DeleteModel(
            name='ProfileDetails',
        ),
    ]
