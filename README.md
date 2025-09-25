
# Gate Pass

A simple School Gate Pass management web application built with Django.  
Provides request creation, approval/rejection workflows and a minimal UI for users and guards/admins.



---

## Table of contents

- [About](#about)  
- [Features](#features)  
- [Tech stack](#tech-stack)  
- [Quick start (dev)](#quick-start-dev)  
- [Environment variables](#environment-variables)  
- [Database](#database)  
- [Project structure](#project-structure)  


---

## About

This repository implements a Gate Pass system using Django with HTML / CSS / JavaScript front-end assets. The repository contains the Django project (likely in `config/`) and application(s) (`gatepass/`, `students/`) plus static assets and admin templates. 

---

## Features (inferred from code layout)
- User authentication (admin + user flows)  
- Create / submit gate pass requests  
- Approve / reject gate pass requests (admin/guard)  
- Pass history / status view for users  
- Web UI templates and static assets (JS/CSS).

---

## Tech stack
- Python (3.8+) — use latest 3.x LTS you support  
- Django (please pin a version; instructions below)  
- Front-end: HTML, CSS, JavaScript (repo languages show heavy HTML/JS/CSS usage). 

> If you want exact pinned dependency versions I can extract them from `requirements.txt` — if not present, see the quick step below to generate one.

---

## Quick start (development)

1. Clone the repo:
```bash
git clone https://github.com/mrtechzw/Gate_Pass.git
cd Gate_Pass
````

2. Create & activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows PowerShell
```

3. Install dependencies:

*  generate `requirements.txt`:

```bash
pip freeze > requirements.txt
```

```bash
pip install -r requirements.txt
```


4. Configure environment variables (see next section).

5. Run migrations:

```bash
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the dev server:

```bash
python manage.py runserver
```

8. Open `http://127.0.0.1:8000/` in the browser.

---



## Database

By default, Django uses SQLite (good for development). For production use PostgreSQL (recommended). Example Postgres `DATABASE_URL`:

```
postgres://USER:PASSWORD@HOST:PORT/DBNAME
```

To switch to Postgres:

1. Install driver: `pip install psycopg2-binary`
2. Update your `DATABASES` or use `dj-database-url` and `DATABASE_URL` env var.

---

## Project structure

```
Gate_Pass/
├─ config/           # Django project settings (settings.py, urls, wsgi/asgi)
├─ gatepass/         # Main app (models, views, templates)
├─ students/         
├─ static/           # css/js/images
├─ templates/admin/  # custom admin templates
├─ manage.py
└─ README.md
```





## Contributing

1. Fork the repo.
2. Create a feature branch.
3. Run tests and linters locally.
4. Submit a PR describing the change.

Please add a `CONTRIBUTING.md` if you expect external contributors.

---



### By Richard Gunha

* Repo root listing (saw top-level folders & files). 
* `manage.py` present. ([GitHub][2])
* `gatepass/` app folder present. ([GitHub][3])
* `gatepass/models.py` exists (app contains Python code). 
* `README.md` placeholder exists (we’re replacing/improving it).

---
