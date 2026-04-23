from django.shortcuts import render
from drf_app.models import *
from drf_app.serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet

@api_view(['GET'])
def student_info(request):
    stud_data = StudentInfoModel.objects.all()
    ser_data = studentserializer(stud_data, many=True)
    return Response({
        "success" : True,
        "message" : "Students Currently Available",
        "data" : ser_data.data
        }, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_student(request):
    if request.method == 'POST':
        serial_data = studentserializer(data = request.data)
        if serial_data.is_valid():
            serial_data.save()
            return Response({
                "success" : True,
                "message" : "New Student Has Been Enlisted Successfully",
                "data" : serial_data.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success" : False,
            "message" : serial_data.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def student_details(request, id):
    try:
        stud_data = StudentInfoModel.objects.get(id=id)
    except StudentInfoModel.DoesNotExist:
        return Response({
            "success" : False,
            "message" : "No Such Student Found",
        }, status=status.HTTP_404_NOT_FOUND)
    
    serial_data = studentserializer(stud_data)
    return Response({
        "success" : True,
        'message' : 'Student has been found',
        'data' : serial_data.data
    }, status=status.HTTP_202_ACCEPTED)

@api_view(['PUT', 'PATCH'])
def update_student(request, id):
    try:
        stud_data = StudentInfoModel.objects.get(id=id)
    except StudentInfoModel.DoesNotExist:
        return Response({
            'success' : False,
            'message' : "Students Couldn't Be Found"
        }, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serial_data = studentserializer(stud_data, data=request.data)
        if serial_data.is_valid():
            serial_data.save()
            return Response({
                "success" : True,
                "message" : "Student Information Updated Successfully.",
                "data" : serial_data.data
            }, status=status.HTTP_202_ACCEPTED)
        return Response({
            "success" : False,
            "message" : serial_data.errors
        }, status=status.HTTP_406_NOT_ACCEPTABLE)
        
    elif request.method == 'PATCH':
        serial_data = studentserializer(stud_data, data=request.data)
        if serial_data.is_valid():
            serial_data.save()
            return Response({
                "success" : True,
                "message" : "Student Information Updated Successfully.",
                "data" : serial_data.data
            }, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response({
            "success" : False,
            "message" :serial_data.errors
        }, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['DELETE'])
def delete_info(request, id):
    try:
        stud_data = StudentInfoModel.objects.get(id = id)
    except StudentInfoModel.DoesNotExist:
        return Response({
            'success' : False,
            'message' : 'No such student info found',
        }, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        stud_data.delete()
        return Response({
            'success' : True,
            'message' : 'Student information has been deleted'
        }, status=status.HTTP_205_RESET_CONTENT)
    
    return Response({
        'success' : True,
        'message' : 'Student no longer exist',
    }, status=status.HTTP_204_NO_CONTENT)
