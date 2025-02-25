# Django DRF Multi-Tenancy with Schema Isolation

A scalable **multi-tenant** system using **Django, Django Rest Framework (DRF), and PostgreSQL** with **schema-level isolation**. Each tenant (a group of companies) gets its own **isolated schema**, ensuring **data security** and **performance optimization**.

---

## 🚀 Features

✅ **Schema-based Multi-Tenancy** – Each tenant has a separate schema in PostgreSQL.  
✅ **Automatic Schema Switching** – Requests are routed to the correct schema dynamically.  
✅ **Shared & Tenant-Specific Apps** – Control which apps are shared vs. tenant-specific.  
✅ **Scalable & Secure** – Supports adding new tenants without modifying existing data.  
✅ **Django & DRF Integration** – Provides APIs for tenant management.  

---

## 🛠 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Epic-Codebase/django_drf_multi_tenancy.git
cd django_drf_multi_tenancy
```

### 2️⃣ Set Up a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure PostgreSQL for Schema Support
Ensure PostgreSQL is installed and create a database:
```sql
CREATE DATABASE multi_tenant_db;
```
Update **`.env`** with database credentials:
```ini
DATABASE_URL=postgres://username:password@localhost:5432/multi_tenant_db
```

### 5️⃣ Apply Migrations
```sh
python manage.py migrate_schemas --shared
```

---

## 🚀 Usage

### 1️⃣ Create a New Tenant
Run the following Django shell command to create a tenant:
```sh
python manage.py shell
```
```python
from tenants.models import Tenant
tenant = Tenant(domain="company1.globaldealer.com", schema_name="company1")
tenant.save()
```
🔹 This will create **a new schema in PostgreSQL** for `company1`.

### 2️⃣ Access Tenant-Specific Data
When a request comes from `company1.globaldealer.com`, Django automatically switches to its schema.

---

## 🔧 Configuration

Modify the **Django settings** to define shared vs. tenant-specific apps:

```python
SHARED_APPS = [
    "django_tenants",
    "users",  # Shared auth system
]

TENANT_APPS = [
    "globaldealer_app",  # Tenant-specific app
]

INSTALLED_APPS = list(set(SHARED_APPS + TENANT_APPS))
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repo  
2. Create a new branch (`feature-branch`)  
3. Submit a Pull Request  

---

## 📜 License

This project is licensed under the MIT License.

