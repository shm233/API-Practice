from django.urls import path
from drf_app.views import *

urlpatterns = [
    path('', student_info, name='student_info'),
    path('add-student/', add_student, name = 'add_new_student'),
    path('student-details/<int:id>/', student_details, name='student_details'),
    path('student-update/<int:id>/', update_student, name='update_student'),
    path('student-delete/<int:id>/', delete_info, name='delete_info'),
]
