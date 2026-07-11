To-Do List App — File Handling Edition

A multi-user command-line To-Do List application built in Python using file handling and JSON for data persistence — no database used. Built to strengthen backend fundamentals before moving to a database-driven version.


Features


User authentication — Signup and Login with email and password validation
Multi-user support — each user gets their own separate JSON file for task storage
Add, view, update, and delete tasks
Mark tasks as complete
Auto-reordering of task IDs after deletion or completion
Pending and completed task count tracking
Pie chart visualization of task statistics using Matplotlib
Input validation — email format, password strength, duplicate username/email checks



Project Structure

App_file_handling/
│
├── app.py           # Entry point — login/signup flow and main loop
├── program.py       # Core task management logic and file operations
├── login_Page.py    # Email and password validation functions
│
├── database.json    # Stores all user records (username, email, password)
├── emails.json      # Stores registered emails
├── usernames.json   # Stores registered usernames
└── <username>.json  # Individual task file per user (created on first login)


How to Run

Requirements


Python 3.x
matplotlib


Install dependencies

bashpip install matplotlib

Run the app

bashpython app.py


How It Works

Signup


User enters a unique username, valid email, and a strong password
Data is saved across three JSON files — database.json, emails.json, usernames.json


Login


Credentials are matched against database.json
On successful login, the user's personal task file (<username>.json) is loaded


Task Management


Tasks are stored as a list of dictionaries inside the user's JSON file
Each task has a task_id and a Task field
Pending and completed counts are tracked and saved with every operation


Data Structure (per user file)

json{
    "tasks": [
        {"task_id": 1, "Task": "Buy groceries"},
        {"task_id": 2, "Task": "Read a book"}
    ],
    "Pending Count": 2,
    "Completed Count": 0
}


Password Requirements


Minimum 8 characters
At least one uppercase letter
At least one lowercase letter
At least one number
At least one special character (!@#$%^&*()+-_.)



Tech Stack


Python 3
JSON for data storage
Matplotlib for visualization
re module for email validation



Planned Improvements


 Password hashing with hashlib
 MongoDB integration for database-backed storage
 Task status field (pending/completed) instead of removal on completion
 Task due dates and priorities
