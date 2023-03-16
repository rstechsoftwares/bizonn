from rest_framework import generics
from API.models import Retailer
from API.serializers import RetailerSerializer
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


# ====== Retailer Views Starts ========
@api_view(['GET'])
def GetAllRetailerView(request):
    AllRetailers = Retailer.objects.all()
    serializer_class = RetailerSerializer(AllRetailers, many=True)
    return Response({"data":serializer_class.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def GetRetailerByIDView(request):
    # Getting retailerID in uuid (Queru Param ?retailerID=)
    retailerID = request.query_params.get('retailer_id')
    # If retailerID is not provided
    if retailerID is None:
        return Response({"data": "Retailer Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        RetailerData = Retailer.objects.get(retailerID=retailerID)
        serializer = RetailerSerializer(RetailerData, many=False)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def CreateRetailerView(request):
    ReqData = request.data
    try:
        serializers = RetailerSerializer(data=ReqData)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(serializers.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['PATCH'])
def UpdateRetailerView(request):
    # Getting productID in uuid (Queru Param ?retailerID=)
    retailerID = request.query_params.get('retailer_id')
    # If retailerID is not provided
    if retailerID is None:
        return Response({"data": "Retailer Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    ReqData = request.data
    try:
        retmodel = Retailer.objects.get(retailerID=retailerID)
        print(retmodel)
        serializers = RetailerSerializer(instance=retmodel,data=ReqData, many=False)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print("Error ==>", err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def DeleteRetailerView(request):
    # Getting retailerID in uuid (Queru Param ?retailerID=)
    retailerID = request.query_params.get('retailer_id')
    # If retailerID is not provided
    if retailerID is None:
        return Response({"data": "Retailer Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        retmodel = Retailer.objects.get(retailerID=retailerID)
        retmodel.delete()
        return Response({"data": "Retailer Model Deleted"}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"msg": err.message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    