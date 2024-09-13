from django.urls import path
from .views import Login, TokenRefreshView,  UserRegistrationView, UserFollow, UserUnfollow

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', Login.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('follow/', UserFollow.as_view()),
    path('unfollow/', UserUnfollow.as_view()),
]