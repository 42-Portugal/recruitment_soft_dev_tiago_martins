# To-Do List API

A simple To-Do List API built with Django and Django REST Framework (DRF).

This API allows the managing of:

* Projects
* Categories
* Tasks

---

## Prerequisites

* Python 3.13+
* pip
* (Optional) Docker & Docker Compose
* (Optional) Make

---

## Quick Start (without Docker)

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd to_do_list
```

2. **Create a virtual environment**

```bash
python3 -m venv venv
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

5. **Run the development server**

```bash
python manage.py runserver
```

6. **Visit the API**

* API root: `http://127.0.0.1:8000/api/`
* Example endpoints:

  * `http://127.0.0.1:8000/api/projects/`
  * `http://127.0.0.1:8000/api/tasks/`
  * `http://127.0.0.1:8000/api/categories/`

---

## Quick Start (with Docker)

1. **Build and run containers**

```bash
docker-compose up --build
```

2. **Apply migrations inside the container**

```bash
docker-compose exec web python manage.py migrate
```

3. **Create a superuser (optional)**

```bash
docker-compose exec web python manage.py createsuperuser
```

4. **Visit the API**

* API root: `http://127.0.0.1:8000/api/`
* Example endpoints:

  * `http://127.0.0.1:8000/api/projects/`
  * `http://127.0.0.1:8000/api/tasks/`
  * `http://127.0.0.1:8000/api/categories/`

---

## Using the Makefile

You can use the provided `Makefile` to simplify common commands:

| Command                | Description                                    |
| ---------------------- | ---------------------------------------------- |
| `make up`              | Build and start the Docker container           |
| `make down`            | Stop and remove the Docker container           |
| `make logs`            | Follow container logs                          |
| `make restart`         | Restart the container                          |
| `make migrate`         | Run Django migrations inside container         |
| `make makemigrations`  | Create Django migrations inside container      |
| `make flush`           | Clear the database (WARNING: deletes all data) |

Example:

```bash
make up
make migrate
make createsuperuser
make logs
```