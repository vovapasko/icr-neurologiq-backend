from rest_framework import serializers
from ..models import FileTemplate


class FileTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileTemplate
        fields = '__all__'
        depth = 1
