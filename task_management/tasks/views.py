from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

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

        # Sorting by due_date or priority
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
