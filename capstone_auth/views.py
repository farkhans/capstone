from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import User

class Register(APIView):
    def post(self, request):
        data = request.data
        repeat_password = data.get('repeat_password')
        
        if (data.get('password') != repeat_password):
            return JsonResponse(
                {
                    'error': 'Password and repeat password do not match'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        username = data.get('username')
        if User.objects.filter(username=username).exists():
            return JsonResponse(
                {
                    'error': f'Username {username} already exists'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = UserSerializer(data=data)

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
                status=status.HTTP_400_BAD_REQUEST
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
    
class UpdateProfileImage(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request):
        user = request.user
        data = request.FILES
        updated_user = User.objects.get(id=user.id)
        updated_user.profile_img = data['profile_img']
        updated_user.save()
        serializer = UserSerializer(updated_user)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        
class GetUser(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)