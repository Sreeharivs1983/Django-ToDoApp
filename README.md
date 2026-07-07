# MyApp

Simple Django todo app.

Running locally with Docker:

```powershell
docker compose up --build -d
docker compose logs -f
```

CI/CD

- The repository includes a CI workflow that runs Django tests on push and PRs: `.github/workflows/ci.yml`.
- The CD workflow builds and pushes a Docker image to GitHub Container Registry on push to `main`/`master`: `.github/workflows/cd.yml`.

Secrets required for CD (using GHCR):

- No extra secret is required if you use the built-in `GITHUB_TOKEN`. If you prefer Docker Hub, create `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` in repo settings and update the workflow to use them.
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

## Docker

Build and run with Docker:

```bash
docker build -t todoapp .
docker run -p 8000:8000 todoapp
```

The app will be available at `http://127.0.0.1:8000/`.

## GitHub Actions

A CI workflow is included at `.github/workflows/docker-ci.yml`.
It installs dependencies, runs migrations, runs tests, and builds the Docker image on every push or pull request to `master`.

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
├── .github/         # GitHub Actions workflows
├── Dockerfile
├── .dockerignore
├── .gitignore
├── manage.py
└── requirements.txt
```
