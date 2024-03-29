from rest_framework import status
from ..models import UploadedPhoto, FileTemplate
from ai.ocr_form import run
from .base_view import BaseView
from rest_framework.generics import ListCreateAPIView
from ..serializers import UploadFileSerializer, FileTemplateSerializer
import os
from webserver.helpers import from_base64_to_content_file


class UploadFileView(BaseView, ListCreateAPIView):
    serializer_class = FileTemplateSerializer
    post_serializer = UploadFileSerializer
    queryset = FileTemplate.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.post_serializer(data=request.data)
            if serializer.is_valid():
                uploaded_file = from_base64_to_content_file(request.data.get('photo'), filename='file')
                template_id = request.data.get('template')
                template_file = FileTemplate.objects.get(id=template_id)
                photo = UploadedPhoto(photo=uploaded_file, template=template_file)
                data = run(
                    par_template_file=template_file.file.file,
                    par_image_file=photo.photo.file,
                    par_locations=template_file.get_locations_list(),
                )
                return self.success_response(data=data, status_code=status.HTTP_201_CREATED)
            else:
                return self.error_response(errors=serializer.errors)

        except Exception as e:
            raise e
