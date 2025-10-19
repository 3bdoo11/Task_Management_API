from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

# --- User Serializers ---

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for registering new users.
    It ensures the password is written only (not read back) and hashed securely.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        # Use the built-in create_user method to ensure the password is hashed
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for read-only user details (e.g., admin or personal profile).
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined')
        read_only_fields = ('username', 'email', 'date_joined')

# --- Task Serializer ---

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.
    The owner field is read-only and shows the username.
    """
    # Use CharField for owner to display the username (read-only)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'title', 'description', 'due_date', 
            'priority', 'status', 'created_at', 'completed_at'
        ]
        # These fields are set automatically or by custom actions/defaults
        read_only_fields = ('status', 'completed_at', 'created_at')
