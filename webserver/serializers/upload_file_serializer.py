# from .file_temlate_serializer import FileTemplateSerializer
from rest_framework import serializers

from ..models import UploadedPhoto


class UploadFileSerializer(serializers.ModelSerializer):
    # photo = serializers.CharField()

    class Meta:
        model = UploadedPhoto
        fields = '__all__'

