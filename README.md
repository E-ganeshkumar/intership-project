# Project Flow

                    ACCOUNTS
                       │
          ┌────────────┴────────────┐
          ↓                         ↓
      EMPLOYER                  CANDIDATE
          │                         │
          │ Login                   │ Login
          ↓                         ↓
    Employer JWT              Candidate JWT
          │                         │
          ↓                         ↓
       JOBS API                JOBS API
          │                         │
    Create Job                     │
          │                         │
          └──────────┐     ┌───────┘
                     ↓     ↓
                  APPLICATION
                     │
                     ↓
              Candidate applies
                     │
                     ↓
             Status = APPLIED
                     │
                     ↓
            Employer views applicant
                     │
                     ↓
              Update status
                     │
          ┌──────────┼──────────┐
          ↓          ↓          ↓
     SHORTLISTED  REJECTED    HIRED

> 1.Create Employer

POST :  http://127.0.0.1:8000/api/users/register/get/

Body :

{
    "username": "employer1",
    "email": "employer@gmail.com",
    "password": "12345678",
    "role": "EMPLOYER",
    "phone": "9876543210"
}

expected Response :

{
    "id": 1,
    "username": "employer1",
    "email": "employer@gmail.com",
    "role": "EMPLOYER",
    "phone": "9876543210"
}

> 2.Create Candidate

POST :  http://127.0.0.1:8000/api/users/register/get/

Body :

{
    "username": "candidate1",
    "email": "candidate@gmail.com",
    "password": "12345678",
    "role": "CANDIDATE",
    "phone": "9876543211"
}

expected Response :

{
    "username": "candidate1",
    "email": "candidate@gmail.com",
    "password": "12345678",
    "role": "CANDIDATE",
    "phone": "9876543211"
}

> 3.Login Employer JWT

POST : http://127.0.0.1:8000/api/users/token/login/

Body : 

{
    "username": "employer1",
    "password": "12345678"
}

expected Response :

{
	"refresh": "  ",
	"access": " "
}

> 4.Login Candidate JWT 

POST : http://127.0.0.1:8000/api/users/token/login/

Body : 

{
    "username": "cndiate1",
    "password": "12345678"
}

expected Response :
{
	"refresh": "  ",
	"access": " "
}

>5.Jobs API create job

POST : http://127.0.0.1:8000/api/jobs/jobscreate

## first in insomnia open Auth and past employertoken
Body : 

{
    "title": "Python Developer",
    "description": "We are looking for a Python Developer",
    "location": "Bangalore",
    "skills": "Python, Django, DRF",
    "salary_min": "300000",
    "salary_max": "600000"
}

expected Response :

[
	{
		"id": 1,
		"employer": 2,
		"employer_name": "employer1",
		"title": "Python Developer",
		"description": "We are looking for a Python Developer",
		"location": "Bangalore",
		"skills": "Python, Django, DRF",
		"salary_min": "300000.00",
		"salary_max": "600000.00",
		"is_active": true,
		"created_at": "2026-09-04T05:38:29.970157Z",
		"updated_at": "2026-09-04T05:38:29.970476Z"
	}
]
 
 >> get data and update and anthing can do in by use only employee token

> 6.Create Application

POST : http://127.0.0.1:8000/api/applications/creatapplications/

## first in insomnia open Auth and past candiatetoken

Body : 
{
    "job": 1,
    "resume": "https://example.com/resume.pdf",
    "cover_letter": "I am interested in this Python Developer position."
}

expected Response :

{
	"id": 1,
	"job": 1,
	"job_title": "Python Developer",
	"candidate": 1,
	"candidate_name": "john_doe",
	"resume": "https://example.com/resume.pdf",
	"cover_letter": "I am interested in this Python Developer position.",
	"status": "APPLIED",
	"applied_at": "2026-09-04T06:19:24.416033Z"
}

> 7.Candidate Checks Their Applications

GET : http://127.0.0.1:8000/api/applications/myapplications/

## first in insomnia open Auth and past candiate Token
expected Response :

[
	{
		"id": 1,
		"job": 1,
		"job_title": "Python Developer",
		"candidate": 1,
		"candidate_name": "john_doe",
		"resume": "https://example.com/resume.pdf",
		"cover_letter": "I am interested in this Python Developer position.",
		"status": "APPLIED",
		"applied_at": "2026-09-04T06:19:24.416033Z"
	}
]

> 8.Employer Checks Applicants

GET : http://127.0.0.1:8000/api/applications/employerapplication/

## first in insomnia open Auth and past employee Token

expected Response :
[
	{
		"id": 1,
		"job": 1,
		"job_title": "Python Developer",
		"candidate": 1,
		"candidate_name": "john_doe",
		"resume": "https://example.com/resume.pdf",
		"cover_letter": "I am interested in this Python Developer position.",
		"status": "APPLIED",
		"applied_at": "2026-09-04T06:19:24.416033Z"
	}
]

>9.Employer Updates Application Status

Patch : http://127.0.0.1:8000/api/applications/statusapplication/1

## first in insomnia open Auth and past employee Token

Body :

{
    "status": "SHORTLISTED"
}

expected Response :

{
	"id": 1,
	"job": 1,
	"job_title": "Python Developer",
	"candidate": 1,
	"candidate_name": "john_doe",
	"resume": "https://example.com/resume.pdf",
	"cover_letter": "I am interested in this Python Developer position.",
	"status": "SHORTLISTED",
	"applied_at": "2026-09-04T06:19:24.416033Z"
}

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
│  
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
