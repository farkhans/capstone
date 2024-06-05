from .models import FoodHistory
from rest_framework import serializers

class FoodHistorySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = FoodHistory
        fields = '__all__'
        extra_kwargs = {
            'user': {'write_only': True}
        }