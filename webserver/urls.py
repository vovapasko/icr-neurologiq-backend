from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('templates/', ListTemplateView.as_view(), name='list_template_view'),
    path('upload/', UploadFileView.as_view(), name='upload_file_view'),
    path('download_csv/', DownloadFileCsvView.as_view(), name='download_file_csv_view'),
    path('download_json/', DownloadFileJsonView.as_view(), name='download_file_json_view')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
