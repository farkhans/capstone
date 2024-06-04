from .models import FoodHistory
from rest_framework import serializers

class FoodHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodHistory
        exclude = ['user']