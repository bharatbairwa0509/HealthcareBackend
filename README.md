
# 🏥 Healthcare Backend API (Django + PostgreSQL)

A Django REST Framework-based backend for managing patients, doctors, and their mappings. It uses JWT for authentication and PostgreSQL as the database.

---

## ⚙️ Setup Instructions (Using Your Own PostgreSQL Database)

### 1. Install PostgreSQL

- Download and install: [https://www.postgresql.org/download/](https://www.postgresql.org/download/)
- Remember your PostgreSQL **username** and **password**

---

### 2. Create a PostgreSQL Database and User

Open your PostgreSQL shell or pgAdmin:

```sql
CREATE DATABASE healthcare_db;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO myuser;
```

---

### 3. Configure `settings.py`

Open `settings.py` and update the `DATABASES` config:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'healthcare_db',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

### 4. Install PostgreSQL Driver

```bash
pip install psycopg2-binary
```

---

### 5. Apply Migrations & Run Server

```bash
python manage.py migrate
python manage.py createsuperuser  # Optional
python manage.py runserver
```

---

## 🚀 API Testing with Thunder Client (or Postman)

> ⚠️ For all **protected endpoints**, include the following header:  
> `Authorization: Bearer <access_token>`

### 🔐 Authentication APIs

#### 1. Register
- `POST /api/auth/register/`
```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "password123"
}
```

#### 2. Login (Get access and refresh tokens)
- `POST /api/auth/login/`
```json
{
  "username": "john",
  "password": "password123"
}
```

**Response:**
```json
{
  "access": "your.jwt.access.token",
  "refresh": "your.jwt.refresh.token"
}
```

#### 3. Refresh Token
- `POST /api/auth/token/refresh/`
```json
{
  "refresh": "your.jwt.refresh.token"
}
```

---

## 👩‍⚕️ Patient Management APIs

| Method | Endpoint                    | Description                      |
|--------|-----------------------------|----------------------------------|
| POST   | `/api/patients/`           | Add a new patient                |
| GET    | `/api/patients/`           | Get all patients (current user) |
| GET    | `/api/patients/<id>/`      | Get specific patient details     |
| PUT    | `/api/patients/<id>/`      | Update patient                   |
| DELETE | `/api/patients/<id>/`      | Delete patient                   |

### Example Body (POST/PUT)
```json
{
  "name": "Alice",
  "age": 30,
  "gender": "Female"
}
```

---

## 👨‍⚕️ Doctor Management APIs

| Method | Endpoint                    | Description                |
|--------|-----------------------------|----------------------------|
| POST   | `/api/doctors/`            | Add a new doctor           |
| GET    | `/api/doctors/`            | Get all doctors            |
| GET    | `/api/doctors/<id>/`       | Get doctor details         |
| PUT    | `/api/doctors/<id>/`       | Update doctor              |
| DELETE | `/api/doctors/<id>/`       | Delete doctor              |

### Example Body (POST/PUT)
```json
{
  "name": "Dr. Smith",
  "specialization": "Cardiology"
}
```

---

## 🔗 Patient-Doctor Mapping APIs

| Method | Endpoint                          | Description                                 |
|--------|-----------------------------------|---------------------------------------------|
| POST   | `/api/mappings/`                 | Assign doctor to patient                    |
| GET    | `/api/mappings/`                 | Get all mappings                            |
| GET    | `/api/mappings/<patient_id>/`    | Get all doctors assigned to a patient       |
| DELETE | `/api/mappings/<mapping_id>/`    | Remove doctor from patient                  |

### Example Mapping Body (POST)
```json
{
  "patient": 1,
  "doctor": 2
}
```

---

## 📌 Notes

- All authenticated routes require a header:  
  ```
  Authorization: Bearer <access_token>
  ```

- Replace `localhost:8000` with your actual host if deployed.

- `<id>` = patient or doctor ID  
  `<mapping_id>` = patient-doctor relationship ID  
  `<patient_id>` = patient ID for filtering assigned doctors

---

### ✅ Thunder Client Tips

1. Use **POST** `/api/auth/login/` to get your token
2. In **Thunder Client**, go to `Auth` tab → select `Bearer Token` → paste your access token
3. Test all APIs using the defined endpoints and JSON bodies


POST /api/auth/register/ -
![Create User](https://github.com/user-attachments/assets/11361be6-dd76-4a50-9faf-e7e4730a9251)


/api/auth/login/ -
![login User](https://github.com/user-attachments/assets/55d4a33d-b539-4c55-8d2f-50a32224309c)

/api/patients/ - 
![save Patients](https://github.com/user-attachments/assets/d450363b-9e83-4d43-8bb8-62df68108b25)


GET /api/patients/  - 
![Get patients](https://github.com/user-attachments/assets/fa13a658-b59a-4481-b0c1-022f61f30211)

like as I upload All ScreenShots 


![get The Doctor Assign](https://github.com/user-attachments/assets/29700e28-957a-4571-a492-7f6aa6cfee7d)
![get The Doctor Assign](https://github.com/user-attachments/assets/ca61c4b1-9e60-43b7-9bc2-8a7feedb6650)
![Delete Doctor](https://github.com/user-attachments/assets/1a159281-70dc-4539-b725-008d51db3053)
![delete Doctor Mapping](https://github.com/user-attachments/assets/2a15919a-3f89-472d-a4aa-c8745dc220ce)
![add Doctor](https://github.com/user-attachments/assets/5951a694-d151-43b1-8004-c4cf6479a219)
![assgin A doctor to Patients](https://github.com/user-attachments/assets/3771ab22-a2b7-4051-ac0a-243799ce1796)





