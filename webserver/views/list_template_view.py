from django.shortcuts import render

from ..models import FileTemplate
from rest_framework.generics import ListAPIView

from ..serializers import FileTemplateSerializer


class ListTemplateView(ListAPIView):
    queryset = FileTemplate.objects.all().order_by('id')
    serializer_class = FileTemplateSerializer
