from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # Show username instead of ID

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'is_completed', 'created_at', 'completed_at', 'user']
        read_only_fields = ['user', 'created_at', 'completed_at']  # prevents user from editing these fields

class UserSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)  # nested serializer to display tasks for each other

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'tasks']  # include tasks in user response.

        