from django.urls import path
from .views import GetUserFoodHistory, CreateFoodHistory
app_name = 'food_history'

urlpatterns = [
    path('get-food-history', GetUserFoodHistory.as_view(), name='get_user_food_history'),
    path('create-food-history', CreateFoodHistory.as_view(), name='create_user_food_history'),
]