from django.urls import path
from .views import Register, Login

app_name = 'auth'

urlpatterns = [
    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
]