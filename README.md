# Job Recruitment API

A RESTful Job Recruitment API built using **Python, Django, Django REST Framework, PostgreSQL, and JWT Authentication**.

### About the Project

A Job Recruitment REST API built using Django, Django REST Framework, and PostgreSQL with JWT authentication.
Employers can create and manage jobs, while candidates can search for jobs and apply securely.
The project includes role-based permissions, duplicate application prevention, applicant management, status updates, validation, and API testing.
.

---

## 🛠️ Tech Stack

| Technology            | Purpose              |
| --------------------- | -------------------- |
| Python                | Programming language |
| Django                | Web framework        |
| Django REST Framework | REST API development |
| PostgreSQL            | Database             |
| Simple JWT            | JWT authentication   |
| django-filter         | Filtering            |
| insomnia              | API testing          |
| Git & GitHub          | Version control      |

---

## 📁 Project Structure

```text
job_recruitment_api/
│
├── manage.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── home/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── users/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│   ├── admin.py
│   └── tests.py
│
├── jobs/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│   ├── admin.py
│   └── tests.py
│
└── applications/
    ├── migrations/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── permissions.py
    ├── admin.py
    └── tests.py
```

---

# ⚙️ Installation

pip install django
pip install djangorestframework 
pip install djangorestframework-simplejwt 
pip install psycopg2-binary 
pip install python-dotenv

## startproject

django-admin startproject home

## apps

py manage.py startapp users
py manage.py startapp applications
py manage.py startapp jobs


## Install dependencies

pip install -r requirements.txt

# 🔧 Database Migration

py manage.py makemigrations
python manage.py migrate

# ▶️ Run the Development Server

python manage.py runserver

---

# 🔐 Security

Sensitive configuration values such as database passwords and secret keys should be stored in environment variables.

The `.env` file should not be committed to GitHub.

---