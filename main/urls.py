from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import HelloWorld, ProtectedView

app_name = 'main'

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloWorld.as_view(), name='hello'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('auth/', include('auth.urls')),
    path('food-history/', include('food_history.urls')),
    path('article/', include('article.urls')),
]