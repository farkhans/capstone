from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer

class Register(APIView):
    def post(self, request): 
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return JsonResponse(
                {
                    'error': 'Please provide both username and password'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        user = authenticate(username=username, password=password)

        if not user:
            return JsonResponse(
                {
                    'error': 'Invalid Credentials'
                    },
                    status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = UserSerializer(user)
        token = RefreshToken.for_user(user)
        return JsonResponse(
            {
                'user': serializer.data,
                'refresh': str(token),
                'access': str(token.access_token),
            },
            status=status.HTTP_200_OK
        )