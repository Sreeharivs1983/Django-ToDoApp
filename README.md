# MyApp — Django Todo

Simple Django todo app. This repository is trimmed to the files needed to
run the app locally with Python and Django.

## Setup (local)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Apply migrations and run the dev server:

```powershell
python manage.py migrate
python manage.py runserver
```

4. Open http://127.0.0.1:8000/ in your browser.

## Admin

Create a superuser:

```powershell
python manage.py createsuperuser
```

## Notes

- Removed Docker, Compose, and CI/CD files to keep the repo minimal for local development.
- If you want Docker or CI back, I can add them on request.
