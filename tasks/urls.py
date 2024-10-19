from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import TaskListCreateView, TaskDetailView, UserListView, UserDetailView, APIRootView

urlpatterns = [
    # Token authentication URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token obtain
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh

    # API root and other URLs
    path('', APIRootView.as_view(), name='api-root'),  # API Root overiew
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),  # list and create tasks
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),  #retrieve, update and delete tasks
    path('users/', UserListView.as_view(), name='user-list'),  #list all users (admin only)
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Retrieve individual user info
]

