# 🐍 Django Basics Project

## ✨ Overview

This repository serves as a **practical introduction to the core fundamentals of the Django Web Framework**. It contains simple project files and apps designed to demonstrate key Django concepts, making it an excellent resource for beginners or anyone looking for quick reference examples.

### Key Topics Covered

* Setting up a Django project and app structure.
* Defining **Models** and working with the Django ORM.
* Creating **Views** and handling HTTP requests.
* Configuring **URLs** (routing).
* Using **Templates** for rendering HTML.
* Introduction to the Django **Admin Interface**.

## 🛠️ Installation and Setup

Follow these steps to get a local copy of this project up and running on your machine.

### Prerequisites

You need **Python** (3.8+) and the `pip` package manager installed.

### Steps

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```
    > **Note:** Replace `your-username/your-repo-name` with the actual path to your repository.

2.  **Create a Virtual Environment**
    It's best practice to use a virtual environment to isolate project dependencies.
    ```bash
    python -m venv venv
    # On Windows:
    # .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Database Migrations**
    Django uses migrations to set up the necessary database tables based on the models.
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser (Optional)**
    If you want to access the Django Admin interface:
    ```bash
    python manage.py createsuperuser
    # Follow the prompts to set username, email, and password
    ```

## 🚀 Running the Project

Start the local development server:

```bash
python manage.py runserver
```

## Main Site: http://127.0.0.1:8000/

## Django Admin: http://127.0.0.1:8000/admin/

Folder/File,Purpose
mysite/,"The main Django project configuration files (settings, WSGI, etc.)."
mysite/,"A reusable Django application demonstrating core concepts (models, views, templates)."
manage.py,Command-line utility for interacting with the project.
db.sqlite3,The default lightweight database file (created after running migrate).
requirements.txt,"Lists all necessary Python dependencies (e.g., Django==4.2.0)."

Command,Description
python manage.py startapp <name>,Creates a new Django app.
python manage.py makemigrations,Detects changes in models and creates migration files.
python manage.py shell,Opens a Python shell configured with the Django environment for database testing.
