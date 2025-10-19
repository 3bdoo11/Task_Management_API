from django.utils import timezone
from rest_framework import generics, permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser

# TaskViewSet with filtering and sorting
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.filter(owner=self.request.user)
        
        # Filtering
        status_filter = self.request.query_params.get('status')
        priority_filter = self.request.query_params.get('priority')
        due_date_filter = self.request.query_params.get('due_date')

        if status_filter:
            queryset = queryset.filter(status=status_filter)
        if priority_filter:
            queryset = queryset.filter(priority=priority_filter)
        if due_date_filter:
            queryset = queryset.filter(due_date=due_date_filter)

        # Sorting
        sort_by = self.request.query_params.get('sort_by')
        if sort_by in ['due_date', 'priority']:
            queryset = queryset.order_by(sort_by)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'])
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        task.status = 'Completed'
        task.completed_at = timezone.now()
        task.save()
        return Response({'status': 'Task marked as complete'})

    @action(detail=True, methods=['post'])
    def mark_incomplete(self, request, pk=None):
        task = self.get_object()
        task.status = 'Pending'
        task.completed_at = None
        task.save()
        return Response({'status': 'Task marked as incomplete'})


# Generic class-based views for ListCreate and RetrieveUpdateDelete
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class MarkTaskCompleteView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.instance.status = 'Completed'
        serializer.instance.completed_at = timezone.now()
        serializer.save()


class MarkTaskIncompleteView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.instance.status = 'Pending'
        serializer.instance.completed_at = None
        serializer.save()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]      
