from django.shortcuts import render
from rest_framework.views import APIView    
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import *

class Login(TokenObtainPairView):
    pass

class RefreshToken(TokenRefreshView):
    pass

class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistationSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()

        UserProfile.objects.create(user=user)

class UserFollow(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user_id = request.data.get('user_id')
        user = User.objects.get(id=user_id)
        request.user.profile.following.add(user)
        return Response({'message': 'User followed successfully'}, status=status.HTTP_200_OK)

class UserUnfollow(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user_id = request.data.get('user_id')
        user = User.objects.get(id=user_id)
        request.user.profile.following.remove(user)
        return Response({'message': 'User unfollowed successfully'}, status=status.HTTP_200_OK)
