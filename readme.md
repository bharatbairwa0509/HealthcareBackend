How to Use Your Own PostgreSQL Database and Password for This Project
Install PostgreSQL
Make sure PostgreSQL is installed on your machine.

Download PostgreSQL

Install and remember your PostgreSQL username and password.

Create a Database
Open your PostgreSQL shell or use a GUI tool like pgAdmin and create a new database for this project. For example, run in psql:

pgsql
Copy
Edit
CREATE DATABASE mydb_health;
Create a PostgreSQL User (Optional)
If you want a specific user for this project, create one:

sql
Copy
Edit
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO myuser;
Update settings.py
In your Django project, open settings.py and find the DATABASES section. Replace with your database info:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'healthcare_db',         # Your database name
        'USER': 'myuser',                # Your PostgreSQL username
        'PASSWORD': 'mypassword',        # Your PostgreSQL password
        'HOST': 'localhost',             # Usually localhost
        'PORT': '5432',                  # Default PostgreSQL port
    }
}
Install PostgreSQL Driver
Make sure psycopg2 is installed (PostgreSQL adapter for Python):

bash
Copy
Edit
pip install psycopg2-binary
Apply Migrations
Run migrations to create the necessary tables in your new database:

bash
Copy
Edit
python manage.py migrate
Create a Superuser (Optional)
To access Django admin or for testing:

bash
Copy
Edit
python manage.py createsuperuser
Run Your Server
Start the development server:

bash
Copy
Edit
python manage.py runserver



Healthcare Backend API Documentation
1. Authentication APIs
1.1 Register a new user
URL: POST http://localhost:8000/api/auth/register/

Description: Register a new user with username, email, and password.

Headers: Content-Type: application/json

Body Example:

json
Copy
Edit
{
  "username": "john",
  "email": "john@example.com",
  "password": "password123"
}
Response: Returns user details or error.

Authentication: No

1.2 Login user
URL: POST http://localhost:8000/api/auth/login/

Description: Login user and get JWT tokens (access and refresh).

Headers: Content-Type: application/json

Body Example:

json
Copy
Edit
{
  "username": "john",
  "password": "password123"
}
Response Example:

json
Copy
Edit
{
  "access": "your.jwt.access.token",
  "refresh": "your.jwt.refresh.token"
}
Authentication: No

1.3 Refresh access token
URL: POST http://localhost:8000/api/auth/token/refresh/

Description: Get a new access token using the refresh token.

Headers: Content-Type: application/json

Body Example:

json
Copy
Edit
{
  "refresh": "your.jwt.refresh.token"
}
Response Example:

json
Copy
Edit
{
  "access": "new.jwt.access.token"
}
Authentication: No

Important Authentication Note:
For all authenticated requests, include the header:
Authorization: Bearer <access_token>

Replace <access_token> with the current valid JWT access token.

If your access token expires, use the refresh token with the refresh endpoint to get a new access token.

2. Patient Management APIs
2.1 Add a new patient
URL: POST http://localhost:8000/api/patients/

Headers:

Content-Type: application/json

Authorization: Bearer <access_token>

Body Example:

json
Copy
Edit
{
  "name": "Alice",
  "age": 30,
  "gender": "Female"
}
Response: Newly created patient object.

2.2 Get all patients created by user
URL: GET http://localhost:8000/api/patients/

Headers:

Authorization: Bearer <access_token>

Response: List of patients.

2.3 Get details of a patient
URL: GET http://localhost:8000/api/patients/<id>/

Headers:

Authorization: Bearer <access_token>

Response: Patient details object.

2.4 Update patient details
URL: PUT http://localhost:8000/api/patients/<id>/

Headers:

Content-Type: application/json

Authorization: Bearer <access_token>

Body Example:

json
Copy
Edit
{
  "name": "Alice Updated",
  "age": 31,
  "gender": "Female"
}
Response: Updated patient object.

2.5 Delete a patient record
URL: DELETE http://localhost:8000/api/patients/<id>/

Headers:

Authorization: Bearer <access_token>

Response: HTTP 204 No Content (success)

3. Doctor Management APIs
3.1 Add a new doctor
URL: POST http://localhost:8000/api/doctors/

Headers:

Content-Type: application/json

Authorization: Bearer <access_token>

Body Example:

json
Copy
Edit
{
  "name": "Dr. Smith",
  "specialization": "Cardiology"
}
Response: Newly created doctor object.

3.2 Get all doctors
URL: GET http://localhost:8000/api/doctors/

Headers:

Authorization: Bearer <access_token>

Response: List of doctors.

3.3 Get doctor details
URL: GET http://localhost:8000/api/doctors/<id>/

Headers:

Authorization: Bearer <access_token>

Response: Doctor details object.

3.4 Update doctor details
URL: PUT http://localhost:8000/api/doctors/<id>/

Headers:

Content-Type: application/json

Authorization: Bearer <access_token>

Body Example:

json
Copy
Edit
{
  "name": "Dr. Smith Updated",
  "specialization": "Neurology"
}
Response: Updated doctor object.

3.5 Delete a doctor record
URL: DELETE http://localhost:8000/api/doctors/<id>/

Headers:

Authorization: Bearer <access_token>

Response: HTTP 204 No Content (success)

4. Patient-Doctor Mapping APIs
4.1 Assign a doctor to a patient (Create mapping)
URL: POST http://localhost:8000/api/mappings/

Headers:

Content-Type: application/json

Authorization: Bearer <access_token>

Body Example:

json
Copy
Edit
{
  "patient": 1,
  "doctor": 1
}
Response: Mapping object created.

4.2 Retrieve all patient-doctor mappings
URL: GET http://localhost:8000/api/mappings/

Headers:

Authorization: Bearer <access_token>

Response: List of all mappings.

4.3 Get all doctors assigned to a specific patient
URL: GET http://localhost:8000/api/mappings/<patient_id>/

Headers:

Authorization: Bearer <access_token>

Response: List of doctor mappings for that patient.

4.4 Remove a doctor from a patient (Delete mapping)
URL: DELETE http://localhost:8000/api/mappings/<mapping_id>/

Headers:

Authorization: Bearer <access_token>

Response: HTTP 204 No Content (success)

Important Notes:
Replace http://localhost:8000 with your actual server URL.

Use the JWT token from login for all authenticated requests in the header as:
Authorization: Bearer <access_token>

If your access token expires, get a new one by posting your refresh token to /api/auth/token/refresh/.

IDs in URLs refer to database primary keys:

<id> for patient or doctor as per context

<mapping_id> for patient-doctor mapping record ID

<patient_id> to get doctors assigned to a patient


