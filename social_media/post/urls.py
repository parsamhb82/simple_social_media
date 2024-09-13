from django.urls import path
from .views import *

urlpatterns = [
    path('post-create/', CreatPostView.as_view()),
    path('post-update/<int:pk>/', PostUpdateView.as_view()),
    path('post-delete/<int:pk>/', PostDeleteView.as_view()),
    path('feed/', FeedView.as_view()),
    path('creat-like/', CreateLike.as_view()),
    path('delete-like/<int:pk>/', DeleteLike.as_view()),
    path('comment-create/', CreatComment.as_view()),
    path('comment-delete/<int:pk>/', DeleteComment.as_view()),
]