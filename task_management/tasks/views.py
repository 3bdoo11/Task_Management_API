from django.utils import timezone
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.contrib.auth.models import User
from .models import Task
from .serializers import (
    TaskSerializer, 
    UserSerializer, 
    UserRegistrationSerializer
)

class UserRegistrationView(generics.CreateAPIView):
    """
    API endpoint for user registration. 
    Allows any user to create a new account (AllowAny permission).
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        """Custom create method to return a success message."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "User registered successfully. Use /api-token-auth/ to log in."}, 
            status=status.HTTP_201_CREATED
        )


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    Access is restricted to Superusers (admins) only.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Only admin users can view the list of all users
    permission_classes = [IsAdminUser] 


class TaskViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing task instances.
    Handles all CRUD operations, plus filtering, sorting, and custom actions.
    """
    serializer_class = TaskSerializer
    # Only authenticated users can access their tasks
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Returns tasks only for the currently authenticated user.
        Also handles filtering and sorting based on query parameters.
        """
        user = self.request.user
        # Filter queryset to show only tasks owned by the current user
        queryset = Task.objects.filter(owner=user)
        
        # --- Filtering ---
        status_filter = self.request.query_params.get('status')
        priority_filter = self.request.query_params.get('priority')
        due_date_filter = self.request.query_params.get('due_date')

        if status_filter:
            # Case-insensitive filtering
            queryset = queryset.filter(status__iexact=status_filter)
        if priority_filter:
            queryset = queryset.filter(priority__iexact=priority_filter)
        if due_date_filter:
            queryset = queryset.filter(due_date=due_date_filter)

        # --- Sorting ---
        sort_by = self.request.query_params.get('sort_by')
        # We manually sort here to avoid issues with required database indexes
        if sort_by == 'due_date':
            queryset = sorted(queryset, key=lambda task: task.due_date if task.due_date else timezone.localdate(), reverse=False)
        elif sort_by == 'priority':
            # Implement custom sort order for priorities
            priority_order = {'High': 3, 'Medium': 2, 'Low': 1}
            queryset = sorted(queryset, key=lambda task: priority_order.get(task.priority, 0), reverse=True)
        else:
             # Default sorting by due date
             queryset = queryset.order_by('due_date')


        return queryset

    def perform_create(self, serializer):
        """
        Force the task owner to be the currently logged-in user.
        """
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'], url_path='mark-complete')
    def mark_complete(self, request, pk=None):
        """Custom endpoint to mark a specific task as Completed."""
        task = self.get_object()
        task.status = 'Completed'
        task.completed_at = timezone.now()
        task.save()
        return Response({'status': 'Task marked as complete'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='mark-incomplete')
    def mark_incomplete(self, request, pk=None):
        """Custom endpoint to mark a specific task as Pending."""
        task = self.get_object()
        task.status = 'Pending'
        task.completed_at = None
        task.save()
        return Response({'status': 'Task marked as incomplete'}, status=status.HTTP_200_OK)
