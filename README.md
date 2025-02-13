
# 🚀 Task Automation API

This is a **Flask-based Task Automation API** that supports user authentication, task management, and background task execution using Celery and Redis.

---

## 📌 Features
✅ **User Authentication (JWT-based)**
✅ **Task Management (Create & Monitor Tasks)**
✅ **PostgreSQL for Data Storage**
✅ **Redis & Celery for Background Processing**
✅ **Production-ready Deployment with Docker & Gunicorn**

---

## 📌 Technologies Used
- **Flask** (Backend Framework)
- **Flask-JWT-Extended** (Authentication)
- **PostgreSQL** (Database)
- **Redis + Celery** (Task Processing)
- **Docker & Docker Compose** (Deployment)
- **Gunicorn** (WSGI Server)

---

## 🔧 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/shashankt1/task-automation-api.git
cd task-automation-api


python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
pip install -r requirements.txt


