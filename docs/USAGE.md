# Usage & Developer Notes

This document contains quick instructions to run and test the Todo app locally.

## Local setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Apply migrations:

```powershell
python manage.py migrate
```

4. Create a superuser (optional):

```powershell
python manage.py createsuperuser
```

5. Run the development server:

```powershell
python manage.py runserver
```

## Running tests

```powershell
python manage.py test
```

## Notes for contributors

- The repo was intentionally trimmed to include only files needed to run locally.
- If you want to re-add Docker or CI, open an issue describing intended configuration.
