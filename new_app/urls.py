from django.urls import path
from new_app.views import *

urlpatterns = [
    path('teacher/', TeacherInfoClass.as_view(), name='Teacher_List'),
]
