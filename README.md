# School Management System API

## **Objective**
Build a **School Management System (SMS) API** using **Django** and **MySQL**.

---

## **Description**
This project implements a **RESTful API** for managing **Schools**, **Students**, and **Teachers** using **Django REST Framework (DRF)** with **MySQL** as the database.  
All CRUD operations, JWT authentication, pagination, filtering, and search features are implemented.

---

## **Implemented Features**

### **1. School Management**
-  CRUD operations for schools  
-  Endpoints:  
  - `GET /api/schools/` – List all schools  
  - `POST /api/schools/` – Add a new school  
  - `PUT /api/schools/{id}/` – Update school details  
  - `DELETE /api/schools/{id}/` – Delete a school  

### **2. Student Management**
-  CRUD operations for students  
-  Students linked to schools via **Foreign Key**  
-  Endpoints:  
  - `GET /api/students/` – List all students  
  - `POST /api/students/` – Add a new student  
  - `PUT /api/students/{id}/` – Update student details  
  - `DELETE /api/students/{id}/` – Remove a student  
-  Pagination for large datasets (`?page=1`)  
-  Filtering and search by school or grade  

### **3. Teacher Management**
-  CRUD operations for teachers  
-  Teachers linked to schools via **Foreign Key**  
-  Endpoints:  
  - `GET /api/teachers/` – List all teachers  
  - `POST /api/teachers/` – Add a new teacher  
  - `PUT /api/teachers/{id}/` – Update teacher details  
  - `DELETE /api/teachers/{id}/` – Remove a teacher  

### **4. Security & Enhancements**
-  JWT authentication for secure API access  
-  Basic validation in serializers  
-  Pagination and filtering for handling large datasets  

---

## **Setup Instructions**

### 1. Clone the Repository

git clone https://github.com/cole15sky/TechYatri-SMS.git

cd TechYatri-SMS


### 2. Create a virtual environment
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure MySQL
brew services start mysql   # macOS
sudo systemctl start mysql  # Linux

### 5. Apply Migrations

python manage.py makemigrations

python manage.py migrate


### 6. Create Superuser (Optional)

python manage.py createsuperuser


### 7. Run the Development Server

python manage.py runserver

API available at: http://127.0.0.1:8000/api/
**### Schools API Endpoints**

<img width="1440" height="790" alt="Screenshot 2025-09-05 at 00 24 05" src="https://github.com/user-attachments/assets/dfec4af2-3ee0-4a72-9079-5adeea1431b4" />

**Teachers API-Endpoints**

<img width="1440" height="740" alt="Screenshot 2025-09-05 at 00 24 41" src="https://github.com/user-attachments/assets/f54eb78b-962d-4311-9378-eb787140b7ff" />


**Students Api Endpoints**

<img width="1440" height="900" alt="485727800-8770f130-bb6b-4743-9b9e-1ad60eaa9580" src="https://github.com/user-attachments/assets/caa2b37f-70bb-45fd-9374-d8314ee87d5c" />



