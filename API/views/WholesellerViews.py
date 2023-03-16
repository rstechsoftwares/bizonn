from rest_framework import generics
from API.models import Wholeseller
from API.serializers import WholesellerSerializer
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


# ====== Wholeseller Views Starts ========
@api_view(['GET'])
def GetAllWholesellerView(request):
    AllWholeseller = Wholeseller.objects.all()
    serializer_class = WholesellerSerializer(AllWholeseller, many=True)
    return Response({"data":serializer_class.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def GetWholesellerByIDView(request):
    # Getting wholesellerID in uuid (Queru Param ?wholesellerID=)
    wholesellerID = request.query_params.get('wholeseller_id')
    # If wholesellerID is not provided
    if wholesellerID is None:
        return Response({"data": "Wholeseller Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        WholesellerData = Wholeseller.objects.get(wholesellerID=wholesellerID)
        serializer = WholesellerSerializer(WholesellerData, many=False)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def CreateWholesellerView(request):
    ReqData = request.data
    try:
        serializers = WholesellerSerializer(data=ReqData)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(serializers.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['PATCH'])
def UpdateWholesellerView(request):
    # Getting wholesellerID in uuid (Queru Param ?wholesellerID=)
    wholesellerID = request.query_params.get('wholeseller_id')
    # If wholesellerID is not provided
    if wholesellerID is None:
        return Response({"data": "Wholeseller Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    ReqData = request.data
    try:
        whomodel = Wholeseller.objects.get(wholesellerID=wholesellerID)
        print(whomodel)
        serializers = WholesellerSerializer(instance=whomodel,data=ReqData, many=False)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print("Error ==>", err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def DeleteWholesellerView(request):
    # Getting wholesellerID in uuid (Queru Param ?wholesellerID=)
    wholesellerID = request.query_params.get('wholeseller_id')
    # If wholesellerID is not provided
    if wholesellerID is None:
        return Response({"data": "Wholeseller Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        whomodel = Wholeseller.objects.get(wholesellerID=wholesellerID)
        whomodel.delete()
        return Response({"data": "Wholeseller Model Deleted"}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"msg": err.message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    