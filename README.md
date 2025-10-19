# Task Management API

## **Project Overview**

The Task Management API is a backend project built with **Django** and **Django REST Framework (DRF)**. It allows users to manage their tasks by creating, reading, updating, deleting, and marking tasks as complete or incomplete. The API enforces **user authentication** and **task ownership**, ensuring each user only accesses their own tasks.

This project simulates a real-world backend developer workflow, including database management, API design, and RESTful principles.

---

## **Features**

### **Task Management (CRUD)**

* Create, read, update, and delete tasks
* Task attributes:

  * `title`
  * `description`
  * `due_date`
  * `priority` (Low, Medium, High)
  * `status` (Pending, Completed)
  * `completed_at` (timestamp)

### **User Management**

* Create, read, update, and delete users
* Unique username and email enforced
* Each user manages their own tasks only

### **Task Actions**

* Mark tasks as complete → sets `status` to Completed and records timestamp
* Mark tasks as incomplete → reverts `status` to Pending and clears timestamp

### **Filtering and Sorting**

* Filter tasks by:

  * `status` (Pending, Completed)
  * `priority`
  * `due_date`
* Sort tasks by:

  * `due_date`
  * `priority`

### **Authentication and Permissions**

* Users must log in to access their tasks
* Task endpoints are private and accessible only by task owners

---

## **Tech Stack**

* Python 3.11
* Django 4.x
* Django REST Framework
* SQLite (default DB; can be swapped for PostgreSQL)
* GitHub for version control

---

## **API Endpoints**

| Endpoint                           | Method    | Description                                                          |
| ---------------------------------- | --------- | -------------------------------------------------------------------- |
| `/api/tasks/`                      | GET       | List all tasks for the logged-in user (supports filters and sorting) |
| `/api/tasks/`                      | POST      | Create a new task                                                    |
| `/api/tasks/<id>/`                 | GET       | Retrieve a single task                                               |
| `/api/tasks/<id>/`                 | PUT/PATCH | Update a task                                                        |
| `/api/tasks/<id>/`                 | DELETE    | Delete a task                                                        |
| `/api/tasks/<id>/mark_complete/`   | POST      | Mark a task as complete                                              |
| `/api/tasks/<id>/mark_incomplete/` | POST      | Mark a task as incomplete                                            |

> Note: All endpoints require **user authentication**.

---

## **Setup Instructions**

1. **Clone the repository**

```bash
git clone https://github.com/3bdoo11/Task_Management_API.git
cd Task_Management_API
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Create a superuser (admin)**

```bash
python manage.py createsuperuser
```

6. **Run the server**

```bash
python manage.py runserver
```

7. **Test the API**

* Use **Postman**, **Insomnia**, or **curl** to interact with your endpoints

---

## **Example API Requests**

**Create a Task**

```json
POST /api/tasks/
{
  "title": "Finish Capstone",
  "description": "Complete Part 4 of the backend project",
  "due_date": "2025-10-25",
  "priority": "High"
}
```

**Mark Task as Complete**

```json
POST /api/tasks/1/mark_complete/
```

**Filter Tasks by Status**

```http
GET /api/tasks/?status=Pending
```

**Sort Tasks by Priority**

```http
GET /api/tasks/?sort_by=priority
```

---

## **Stretch Goals 

* Task Categories (Work, Personal)
* Recurring Tasks (daily, weekly)
* Email or in-app notifications for upcoming due dates
* Task history to track completed tasks
* Collaborative tasks shared among multiple users

---


