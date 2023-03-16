from rest_framework import generics
from API.models import Manufacturer
from API.serializers import ManufacturerSerializer
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


# ====== Manufacturer Views Starts ========
@api_view(['GET'])
def GetAllManufacturerView(request):
    AllManufacturer = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer(AllManufacturer, many=True)
    return Response({"data":serializer_class.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def GetManufacturerByIDView(request):
    # Getting manufacturerID in uuid (Queru Param ?manufacturerID=)
    manufacturerID = request.query_params.get('manufacturer_id')
    # If manufacturerID is not provided
    if manufacturerID is None:
        return Response({"data": "Manufacturer Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        ManufacturerData = Manufacturer.objects.get(manufacturerID=manufacturerID)
        serializer = ManufacturerSerializer(ManufacturerData, many=False)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def CreateManufacturerView(request):
    ReqData = request.data
    try:
        serializers = ManufacturerSerializer(data=ReqData)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(serializers.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['PATCH'])
def UpdateManufacturerView(request):
    # Getting manufacturerID in uuid (Queru Param ?manufacturerID=)
    manufacturerID = request.query_params.get('manufacturer_id')
    # If manufacturerID is not provided
    if manufacturerID is None:
        return Response({"data": "Manufacturer Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    ReqData = request.data
    try:
        manumodel = Manufacturer.objects.get(manufacturerID=manufacturerID)
        print(manumodel)
        serializers = ManufacturerSerializer(instance=manumodel,data=ReqData, many=False)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print("Error ==>", err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def DeleteManufacturerView(request):
    # Getting manufacturerID in uuid (Queru Param ?manufacturerID=)
    manufacturerID = request.query_params.get('manufacturer_id')
    # If manufacturerID is not provided
    if manufacturerID is None:
        return Response({"data": "Manufacturer Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        manumodel = Manufacturer.objects.get(manufacturerID=retailmanufacturerIDerID)
        manumodel.delete()
        return Response({"data": "Manufacturer Model Deleted"}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"msg": err.message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    