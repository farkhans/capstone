from django.db import models
from capstone_auth.models import User
from django.core.validators import MinValueValidator

class FoodHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.CharField(max_length=100)
    date = models.DateField()
    meal_type = models.CharField(max_length=255)
    calories = models.FloatField(validators=[MinValueValidator(0.0)])