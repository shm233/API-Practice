from rest_framework import serializers
from drf_app.models import *

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfoModel
        fields = '__all__'

        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for f in self.field.value():
                f.widget.attrs.update({'class':'form-control'})
