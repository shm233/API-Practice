from rest_framework import serializers
from new_app.models import *

class TeacherInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherInfoModel
        fields = '__all__'
        