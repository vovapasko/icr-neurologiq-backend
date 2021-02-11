from .download_file_view import DownloadFileView
from ..serializers.json_data_serializer import JsonDataSerializer
import json


class DownloadFileCsvView(DownloadFileView):
    serializer_class = JsonDataSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            json_str = json.dumps(serializer.data.get('data'))
            path = 'results.csv'
            content_type = 'text/csv'
            return super().get_file(request, json_str, path, content_type, *args, **kwargs)
        return self.error_response(errors=serializer.errors)
