from .download_file_view import DownloadFileView


class DownloadFileJsonView(DownloadFileView):
    def get(self, request, *args, **kwargs):
        path = 'results.json'
        content_type = 'application/json'
        return super().get_file(request, path, content_type, *args, **kwargs)
