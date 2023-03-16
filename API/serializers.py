from rest_framework import serializers
from .models import Product, Category, Retailer, Manufacturer, Wholeseller

# serializer for Product Model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    # for partial updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(ProductSerializer, self).__init__(*args, **kwargs)

# serializer for Profile Details Model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    # for partial updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(CategorySerializer, self).__init__(*args, **kwargs)

# serializer for Retailer Model
class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = '__all__'

    # for partial updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(RetailerSerializer, self).__init__(*args, **kwargs)


# serializer for Manufacturer Model
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

    # for partial updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(ManufacturerSerializer, self).__init__(*args, **kwargs)

# serializer for wholeseller Model
class WholesellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wholeseller
        fields = '__all__'

    # for partial updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(WholesellerSerializer, self).__init__(*args, **kwargs)
