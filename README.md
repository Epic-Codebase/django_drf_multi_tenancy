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

## **Understanding Schema-Based Multi-Tenancy in Django & DRF**

## **How Schema-Based Multi-Tenancy Works**
Schema-based multi-tenancy is an approach where **each tenant (company) has its own isolated schema** in a single PostgreSQL database. This ensures **data security, isolation, and scalability** while allowing shared authentication and cross-tenant management when required.

Unlike row-based multi-tenancy (where all tenants share the same tables), schema-based multi-tenancy provides:
- **Strong Isolation** – Each company’s data exists in a separate schema.
- **Better Performance** – Queries operate on smaller, tenant-specific tables.
- **Easier Scaling** – Adding a new tenant means creating a new schema without affecting existing tenants.

## **Multi-Tenancy Structure in Global Dealer**
The **Global Dealer** product supports two types of customers:

1. **Single-Company Customers** – One company (one schema) with multiple users.
2. **Conglomerate Customers** – A parent organization with multiple companies (tenants), each having its own schema.
3. **Tenant-Based Users**:
   - **Admin Users** – Manage their specific company (tenant).
   - **Regular Users** – Belong to a specific company.

### **Schema Design Example**
Here’s an example of how PostgreSQL schemas will be structured:

```
public (shared schema)
│── tenants (stores metadata about all tenants)
│── users (shared authentication system)
│
├── company_1 (tenant schema)
│   ├── projects
│   ├── orders
│   ├── invoices
│
├── company_2 (tenant schema)
│   ├── projects
│   ├── orders
│   ├── invoices
│
├── company_3 (tenant schema)
│   ├── projects
│   ├── orders
│   ├── invoices
```

Each **tenant schema** (`company_1`, `company_2`, etc.) contains the same **isolated tables**. The `public` schema holds **shared tables**, like user authentication.

## **Handling Tenant Routing in Django**
To manage multi-tenancy, Django will dynamically **switch schemas based on the request**. This is done using middleware that detects the tenant from the request domain and activates the corresponding schema.

**Example Middleware Flow:**
1. User requests `company1.globaldealer.com`.
2. Middleware identifies `company1` as the tenant.
3. Django switches to the `company_1` schema.
4. The request is processed using `company_1`'s data.



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

