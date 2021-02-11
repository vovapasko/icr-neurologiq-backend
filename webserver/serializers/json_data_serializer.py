from rest_framework import serializers


class JsonDataSerializer(serializers.Serializer):
    data = serializers.JSONField()
