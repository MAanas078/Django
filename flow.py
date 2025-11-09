# Step 1: User Opens Website

# Action:
# User visits → http://127.0.0.1:8000/

# Flow:

# Browser sends GET request to Django server.

# Django checks urls.py to find which view function should handle /.

# ✅ Django routes the request to → view_function() function in views.py.

# Step 2: View Fetches Data from Model

# Action:
# In views.py, Django runs the logic of view function:

# from .models import Task

# def index(request):
#     tasks = Task.objects.all()  # Fetch all tasks from database
#     return render(request, 'index.html', {'tasks': tasks})

# Task.objects.all() → Django ORM query to fetch data from SQLite database.

# Data is stored in variable tasks (a list of task objects).

# View then calls render() to send this data to the template.

# ✅ Now Django will render index.html, giving it the context {'tasks': tasks}.

#Step 3: Template Displays Data

# In index.html, you use Django Template Language (DTL):

# <ul>
#   {% for task in tasks %}
#      <li>{{ task.title }}</li>
#   {% endfor %}
# </ul>

# Flow:

# Django replaces {{ task.title }} with actual data fetched from DB.

# The template becomes pure HTML (no Django code now).

# Django sends that HTML back to the browser.

# ✅ User now sees all tasks displayed.


#USER (browser)
#    ↓
# URL → maps to VIEW (views.py)
#    ↓
# VIEW → talks to MODEL (models.py)
#    ↓
# MODEL → fetches/updates DB (SQLite)
#    ↓
# VIEW → renders TEMPLATE (HTML)
#    ↓
# TEMPLATE → returned to USER (browser)



# #Model ↔ Database → handles storage

# View ↔ Model → handles logic

# Template ↔ View → handles display


# Example of Real Flow

# “User adds a task → Django saves it → shows updated list”

# index.html form → sends POST

# add_task() view → saves via ORM

# Database updated

# Redirects → index() view

# Fetches all tasks

# Template renders list




