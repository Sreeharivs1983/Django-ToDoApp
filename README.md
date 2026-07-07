# Todo List App

A clean, modern to-do list application built with Django.

## Features

- Add, edit, and delete tasks
- Mark tasks as complete/incomplete
- Priority levels (Low, Medium, High)
- Optional due dates and descriptions
- Filter by All, Active, or Completed
- Clear all completed tasks at once
- Django admin panel for management

## Setup

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run migrations**

   ```bash
   python manage.py migrate
   ```

3. **Start the development server**

   ```bash
   python manage.py runserver
   ```

4. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Optional: Admin Panel

Create a superuser to access the admin at `/admin/`:

```bash
python manage.py createsuperuser
```

## Project Structure

```
MyApp/
├── config/          # Django project settings
├── todos/           # Todo app (models, views, forms)
├── templates/       # HTML templates
├── manage.py
└── requirements.txt
```
