"""
URL configuration for task_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
URL configuration for task_management project.
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework.authtoken.views import obtain_auth_token 

def home(request):
    """Simple API status check endpoint."""
    return JsonResponse({
        "message": "Welcome to Task Management API", 
        "endpoints": {
            "tasks_and_users": "/api/",
            "register": "/api/users/register/",
            "login": "/api-token-auth/",
            "admin": "/admin/"
        }
    })

urlpatterns = [
    # 1. Django Admin Interface
    path('admin/', admin.site.urls),
    
    # 2. Base API Endpoints (Delegates to tasks/urls.py, which uses the router)
    path('api/', include('tasks.urls')),
    
    # 3. Authentication Endpoint: Login to get a token (username & password POST)
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
    
    # 4. Root Endpoint (Welcome message)
    path('', home, name='home'),
]


