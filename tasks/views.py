from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse
from rest_framework.permissions import AllowAny
from rest_framework.reverse import reverse  # Use DRF's reverse

class APIRootView(APIView):
    """
    API Root View
    """
    permission_classes = [permissions.AllowAny]  # Allow anyone to view the API root

    def get(self, request, format=None):
        return Response({
            'tasks': reverse('task-list-create', request=request),
            'users': reverse('user-list', request=request),
            'token_obtain_pair': reverse('token_obtain_pair', request=request),
            'token_refresh': reverse('token_refresh', request=request),
        })

# Task CRUD views
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Assign the current user to the task

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

# User CRUD views
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admin can view all users

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

