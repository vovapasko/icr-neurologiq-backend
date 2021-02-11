import os

from django.db import models
from ..models import FileTemplate


class UploadedPhoto(models.Model):
    photo = models.FileField(upload_to='media/')
    template = models.ForeignKey(FileTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return self.photo.name

    def get_path(self):
        return self.photo.path
