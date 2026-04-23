from django.db import models

class TeacherInfoModel(models.Model):
    teac_name = models.CharField(max_length=255, null=True)
    teac_email = models.EmailField(unique=True, null=True)
    teac_id = models.PositiveIntegerField(unique=True)
    teac_address = models.TextField(null=True)
    teac_contact = models.CharField(null=True)
    teac_age = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return f"{self.teac_name}"
