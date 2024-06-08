from django.urls import path
from .views import Register, Login, UpdateProfileImage, GetUser

app_name = 'capstone_auth'

urlpatterns = [
    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('update-profile-image', UpdateProfileImage.as_view(), name='update_profile_image'),
    path('get-user', GetUser.as_view(), name='get_user'),
]