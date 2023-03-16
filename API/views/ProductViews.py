from rest_framework import generics
from API.models import Product
from API.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi
from django.contrib.auth.hashers import make_password
from rest_framework import mixins
from rest_framework.parsers import JSONParser
from django.http import JsonResponse


# This Helps To Develop CRUD APIs Of UserModel (All at one set)


# ====== Product Views Starts ========
@api_view(['GET'])
def GetAllProductView(request):
    AllProducts = Product.objects.all()
    serializer_class = ProductSerializer(AllProducts, many=True)
    return Response({"data":serializer_class.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def GetProductByIDView(request):
    # Getting serviceId in uuid (Queru Param ?productID=)
    productID = request.query_params.get('product_id')
    # If productID is not provided
    if productID is None:
        return Response({"data": "Product Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        ProductData = Product.objects.get(productID=productID)
        serializer = ProductSerializer(ProductData, many=False)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def CreateProductView(request):
    ReqData = request.data
    try:
        serializers = ProductSerializer(data=ReqData)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(serializers.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['PATCH'])
def UpdateProductView(request):
    # Getting productID in uuid (Queru Param ?productID=)
    productID = request.query_params.get('product_id')
    # If productID is not provided
    if productID is None:
        return Response({"data": "Product Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    ReqData = request.data
    try:
        promodel = Service.objects.get(productID=productID)
        print(promodel)
        serializers = ProductSerializer(instance=promodel,data=ReqData, many=False)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print("Error ==>", err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def DeleteProductView(request):
    # Getting promodel in uuid (Queru Param ?promodel=)
    promodel = request.query_params.get('product_id')
    # If promodel is not provided
    if promodel is None:
        return Response({"data": "Product Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        promodel = Product.objects.get(productID=productID)
        promodel.delete()
        return Response({"data": "Product Model Deleted"}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"msg": err.message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    