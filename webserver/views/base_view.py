from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class BaseView(APIView):
    def error_response(self, errors, status_code=status.HTTP_400_BAD_REQUEST):
        return Response(data=errors, status=status_code)

    def success_response(self, data, status_code=status.HTTP_200_OK):
        return Response(data=data, status=status_code)
