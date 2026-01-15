📄 Document Workflow Management System (DWMS)
A production-ready Document Workflow Management System built with Django 3.2 + Django REST Framework + JWT, supporting multi-step approvals, RBAC, audit logging, and Postman-testable APIs.

DWMS is a scalable Django REST-based system enabling document approvals through configurable workflows, role-based access, and audit-grade tracking.

🚀 Features

JWT Authentication (Login / Refresh)

Custom User Model with Roles

Document Upload & Management

Configurable Approval Workflows

Multi-step Approval Engine

Role-Based Access Control (RBAC)

Audit Logs for Compliance

PostgreSQL Support

API-first design (Postman friendly)

🛠 Tech Stack

Python 3.x

Django 3.2.25

Django REST Framework

SimpleJWT

PostgreSQL

Postman (for API testing)

📁 Project Structure
document_workflow/
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── documents/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── workflows/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── engine.py
│   ├── urls.py
│
├── audit/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── document_workflow/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py

🔐 Authentication (JWT)
1️⃣ Login

POST

/api/auth/login/


Request

{
  "username": "admin",
  "password": "admin123"
}


Response

{
  "refresh": "jwt_refresh_token",
  "access": "jwt_access_token"
}

2️⃣ Refresh Token

POST

/api/auth/refresh/


Request

{
  "refresh": "jwt_refresh_token"
}


Response

{
  "access": "new_access_token"
}

👤 User APIs (Accounts)
3️⃣ List Users

GET

/api/users/


Headers

Authorization: Bearer <access_token>


Response

[
  {
    "id": 1,
    "username": "admin",
    "role": "ADMIN"
  }
]

📄 Document APIs
4️⃣ Create Document

POST

/api/documents/


Headers

Authorization: Bearer <access_token>
Content-Type: multipart/form-data


Request

{
  "title": "HR Policy",
  "file": "<uploaded_file>"
}


Response

{
  "id": 1,
  "title": "HR Policy",
  "status": "DRAFT",
  "created_by": 1
}

5️⃣ List Documents

GET

/api/documents/


Response

[
  {
    "id": 1,
    "title": "HR Policy",
    "status": "IN_REVIEW"
  }
]

6️⃣ Get Document Detail

GET

/api/documents/{id}/

🔄 Workflow APIs
7️⃣ Create Workflow

POST

/api/workflows/


Request

{
  "name": "Document Approval Workflow"
}

8️⃣ Add Workflow Steps

POST

/api/workflows/steps/


Request

{
  "workflow": 1,
  "step_order": 1,
  "required_role": "REVIEWER"
}

{
  "workflow": 1,
  "step_order": 2,
  "required_role": "APPROVER"
}

9️⃣ Assign Workflow to Document

POST

/api/workflows/assign/


Request

{
  "document_id": 1,
  "workflow_id": 1
}


Response

{
  "message": "Workflow assigned successfully"
}

🔟 Approve / Reject Document

POST

/api/workflows/action/{document_id}/


Request

{
  "action": "approve"
}


or

{
  "action": "reject"
}


Response

{
  "status": "success",
  "current_step": 2
}

🧾 Audit APIs
1️⃣1️⃣ List Audit Logs

GET

/api/audit/


Response

[
  {
    "id": 1,
    "user": "admin",
    "action": "DOCUMENT_CREATED",
    "document_id": 1,
    "timestamp": "2026-01-15T10:30:00Z"
  }
]

🔒 Authorization Rules
Role	Permissions
ADMIN	Full Access
CREATOR	Create Documents
REVIEWER	Review Documents
APPROVER	Final Approval
▶️ Running the Project
git clone <repo_url>
cd document_workflow

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

🧪 Postman Testing Flow (Recommended)

Login → Get JWT token

Create Document

Create Workflow

Add Workflow Steps

Assign Workflow to Document

Approve / Reject

Verify Audit Logs
