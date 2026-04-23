from django.db import models

class StudentInfoModel(models.Model):
    stud_name = models.CharField(max_length=255, null=True)
    stud_email = models.EmailField(unique=True, null=True)
    stud_id = models.PositiveIntegerField(unique=True)
    stud_address = models.TextField(null=True)
    stud_contact = models.CharField(null=True)
    stud_age = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return f'{self.stud_name} {self.stud_contact}'
