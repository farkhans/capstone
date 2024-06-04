from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from .models import FoodHistory
from .serializers import FoodHistorySerializer

class GetUserFoodHistory(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        food_history = FoodHistory.objects.filter(user=request.user)
        return JsonResponse(
            FoodHistorySerializer(food_history, many=True).data,
            status=status.HTTP_200_OK,
            safe=False
        )
    
class CreateFoodHistory(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['user'] = request.user.pk
        serializer = FoodHistorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )