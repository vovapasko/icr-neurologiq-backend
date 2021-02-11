from django.http import HttpResponse

from .base_view import BaseView


class DownloadFileView(BaseView):
    def get_file(self, request, json: str, path: str, content_type: str, *args, **kwargs):
        response = HttpResponse(json, content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename=' + path
        return response
