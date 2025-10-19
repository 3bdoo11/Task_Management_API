Task Management API (Capstone Project)

Project Overview

The Task Management API is a robust backend solution built using Django and Django REST Framework (DRF). It provides a secure, token-authenticated system for users to manage their personal tasks, complete with deadlines, priority levels, and status tracking.

This project demonstrates proficiency in building a RESTful service, handling authentication, implementing custom logic (filtering, sorting, status updates), and enforcing object-level permissions (users can only access their own tasks).

🚀 Key Features

Feature

Details

User Authentication

Secure registration (/api/users/register/) and token-based login (/api-token-auth/).

Task CRUD

Full Create, Read, Update, and Delete capabilities for tasks.

Task Ownership

Strictly enforced: a user can only view, modify, or delete tasks they own.

Status Actions

Custom endpoints to explicitly set a task status to Completed or Pending, automatically managing the completed_at timestamp.

Filtering

Filter tasks by status (Pending/Completed), priority (Low/Medium/High), or specific due_date.

Sorting

Sort task lists by due_date or priority.

🛠️ Tech Stack

Backend: Python 3.11+

Framework: Django 5.2.5

API: Django REST Framework (DRF)

Database: SQLite (default for development)

Authentication: DRF Token Authentication

🌐 API Endpoints

All endpoints under /api/tasks/ require a Token in the Authorization: Token <key> header, obtained from /api-token-auth/.

Route

Method

Description

/api/users/register/

POST

Public. Creates a new user account.

/api-token-auth/

POST

Public. Logs in a user with username/password and returns an authentication token.

/api/tasks/

GET

Private. Lists all tasks for the authenticated user. Supports filtering/sorting via query params.

/api/tasks/

POST

Private. Creates a new task, automatically assigning the authenticated user as the owner.

/api/tasks/<id>/

GET/PUT/PATCH/DELETE

Private. Retrieve, fully update (PUT), partially update (PATCH), or delete a specific task.

/api/tasks/<id>/mark-complete/

POST

Private. Custom action to set the task status to Completed and record completed_at.

/api/tasks/<id>/mark-incomplete/

POST

Private. Custom action to set the task status back to Pending and clear completed_at.

⚙️ Setup and Installation

Follow these steps to get the project running locally:

Clone the repository:

git clone https://github.com/3bdoo11/Task_Management_API.git
cd Task_Management_API



Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate # macOS/Linux
# venv\Scripts\activate # Windows



Install dependencies:

pip install -r requirements.txt



Apply database migrations:

python manage.py makemigrations tasks
python manage.py migrate



Create an administrative user (optional):

python manage.py createsuperuser



Run the development server:

python manage.py runserver



The API will now be running on http://127.0.0.1:8000/.

🧪 Example Usage (Testing with Postman/Insomnia)

1. Register a User (Initial Setup)

Route

Method

Body

/api/users/register/

POST

{"username": "testuser", "email": "test@example.com", "password": "securepassword123"}

2. Get Authentication Token (Login)

Route

Method

Body

/api-token-auth/

POST

{"username": "testuser", "password": "securepassword123"}

Response: {"token": "YOUR_AUTH_TOKEN_HERE"} (Save this token!)





3. Create Sample Tasks

Ensure you add the header Authorization: Token YOUR_AUTH_TOKEN_HERE for each POST request below.

Route

Method

Task Title & Priority

Body (Example)

/api/tasks/

POST

High Priority: Capstone Submission

{"title": "Finalize Capstone Video and Submit", "description": "Ensure presentation is under 5 minutes.", "due_date": "2025-10-20", "priority": "High"}

/api/tasks/

POST

Medium Priority: Update Dependencies

{"title": "Review requirements.txt", "description": "Check for any outdated packages in the virtual environment.", "due_date": "2025-10-25", "priority": "Medium"}

/api/tasks/

POST

Low Priority: Clean up comments

{"title": "Remove unused code and comments", "description": "Tidy up the views.py and models.py files.", "due_date": "2025-11-01", "priority": "Low"}

4. Filter and Sort Tasks

Ensure you use the Authorization Header.

Route

Method

Description

/api/tasks/?status=Pending

GET

Filters tasks not yet completed.

/api/tasks/?sort_by=priority

GET

Sorts tasks by High, Medium, then Low priority.

5. Mark a Task as Complete (Assuming ID is 1)

Route

Method

Body

/api/tasks/1/mark-complete/

POST

(Empty body)