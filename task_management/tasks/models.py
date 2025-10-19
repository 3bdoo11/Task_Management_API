from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Define choices for the Task Priority field
PRIORITY_CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
]

# Define choices for the Task Status field
STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
]

class Task(models.Model):
    """
    Represents a task associated with a user.
    """
    # The owner of the task. If the user is deleted, all their tasks are also deleted.
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    # Date fields
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    # Status and Priority fields
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    class Meta:
        ordering = ['due_date', '-priority']
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return f"{self.title} ({self.owner.username})"
