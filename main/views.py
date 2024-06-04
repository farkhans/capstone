from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class HelloWorld(APIView):
    def get(self, _):
        return JsonResponse(
            {
                'message': 'Hello, world!'
            },
            status=status.HTTP_200_OK
        )
    
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, _):
        return JsonResponse(
            {
                'message': 'You are authenticated!'
            },
            status=status.HTTP_200_OK
        )