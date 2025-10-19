from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDeleteView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/mark_complete/', views.MarkTaskCompleteView.as_view(), name='task-complete'),
    path('tasks/<int:pk>/mark_incomplete/', views.MarkTaskIncompleteView.as_view(), name='task-incomplete'),
]
