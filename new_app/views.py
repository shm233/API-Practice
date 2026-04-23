from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from new_app.models import *
from new_app.serializers import *

class TeacherInfoClass(APIView):
    def get_object(self, id):
        try:
            return TeacherInfoModel.objects.get(id=id)
        except TeacherInfoModel.DoesNotExist:
            return None
        
    def get(self, request, pk=None):
        if not pk:
            tea_d = TeacherInfoModel.objects.all()
            tea_serial = TeacherInfoSerializer(tea_d, many=True)
            return Response({
                'success' : True,
                'message' : 'Teacher Info Found',
                'data' : tea_serial.data,
            }, status=status.HTTP_302_FOUND)
        else:
            tea_d = self.get_object(pk)
            
            if tea_d:
                tea_serial = TeacherInfoSerializer(tea_d)
                return Response({
                    'success' : True,
                    'message' : 'Teacher Found Successfully',
                    'data' : tea_serial.data,
                }, status=status.HTTP_302_FOUND)
    
    def post(self, request):
        tea_serial = TeacherInfoSerializer(data = request.data)
        if tea_serial.is_valid():
            tea_serial.save()
            return Response({
                'sucess' : True,
                'message' : 'New Teacher Added Successfully',
                'data' : tea_serial.data
            }, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk):
        tea_d = self.get_object(pk)

        if tea_d:
            tea_serial = TeacherInfoSerializer(tea_d, data = request.data)
            if tea_serial.is_valid():
                tea_serial.save()
                return Response({
                    'success' : True,
                    'message' : 'Teacher Info has been updated',
                    'data' : tea_serial.data,
                }, status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            return Response({
                'success' : True,
                'message' : 'Where did the Teacher go',
            }, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        tea_d = self.get_object(pk)
        if tea_d:
            tea_d.delete()
            return Response({
                'successs' : True,
                'message' : 'Teacher has been removed from society',
            }, status=status.HTTP_402_PAYMENT_REQUIRED)
