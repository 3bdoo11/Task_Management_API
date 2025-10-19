
# Task Management API

## Overview

This is a **Task Management API** built with **Django** and **Django REST Framework (DRF)**.
It allows users to manage their tasks by creating, updating, deleting, and marking tasks as complete or incomplete. Each user can only access their own tasks.

---

## Features

* **User Management**: Register, login, and manage user accounts
* **Task CRUD**: Create, Read, Update, Delete tasks
* **Task Status**: Mark tasks as **Completed** or **Pending**
* **Filtering & Sorting**: Filter tasks by status, priority, or due date; sort by priority or due date
* **Permissions**: Users can only access their own tasks

---

## Models

### Task

* `title` (string) – task title
* `description` (text) – task description
* `due_date` (date) – due date
* `priority` (choice) – Low, Medium, High
* `status` (choice) – Pending, Completed
* `completed_at` (datetime) – timestamp when task is completed
* `owner` (User) – user who owns the task

### User

* `username` (string) – unique username
* `email` (string) – unique email
* `password` (string) – hashed password

---

## API Endpoints

| Endpoint                           | Method | Description                               |
| ---------------------------------- | ------ | ----------------------------------------- |
| `/api/tasks/`                      | GET    | List all tasks for the authenticated user |
| `/api/tasks/`                      | POST   | Create a new task                         |
| `/api/tasks/<id>/`                 | GET    | Retrieve a single task                    |
| `/api/tasks/<id>/`                 | PUT    | Update a task                             |
| `/api/tasks/<id>/`                 | DELETE | Delete a task                             |
| `/api/tasks/<id>/mark_complete/`   | POST   | Mark a task as completed                  |
| `/api/tasks/<id>/mark_incomplete/` | POST   | Mark a task as pending                    |

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/3bdoo11/Task_Management_API.git
cd Task_Management_API
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the server:

```bash
python manage.py runserver
```

---

## Usage

* Access API endpoints with an authenticated user
* Use tools like **Postman** or **curl** to test endpoints
* Only the owner of a task can edit or delete it

---

## Future Improvements

* Add **JWT authentication**
* Task categories and recurring tasks
* Notifications for upcoming due dates
* Deployment to **Heroku/PythonAnywhere**

---

