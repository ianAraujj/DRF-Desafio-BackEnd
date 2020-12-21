from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from account.views import UserCreateAPIView

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', UserCreateAPIView.as_view())
]
