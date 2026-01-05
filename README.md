# 📊 Employee Management System (EMS)

### A Full-Stack Cloud-Native Web Application

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791)
![Status](https://img.shields.io/badge/Status-Deployed-success)

## 📖 Project Overview
This project is a robust **Employee Management System** designed to streamline HR operations. Unlike simple file-based applications, this system utilizes a **3-Tier Architecture** connecting a Python frontend to a cloud-hosted **PostgreSQL database**.

It features secure authentication, role-based access control (RBAC), and interactive data visualization, making it a scalable solution for modern enterprise management.

## 🚀 Key Features
* **🔐 Secure Authentication:** User login system with password hashing (`bcrypt`) to ensure security.
* **🛡️ Role-Based Access Control (RBAC):**
    * **Admins:** Full access to Add, Edit, Delete employees and manage system users.
    * **Employees:** Read-only access to the directory and analytics.
* **☁️ Cloud Database Integration:** Data is persisted in a PostgreSQL database (Neon/Supabase), ensuring no data loss on deployment.
* **📈 Real-Time Analytics:** Interactive dashboards using **Plotly** to visualize payroll distribution and department headcount.
* **⚡ CRUD Operations:** Full capability to Create, Read, Update, and Delete records dynamically.

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Interactive web UI framework |
| **Backend Logic** | Python | Core application logic |
| **Database** | PostgreSQL | Relational database (Hosted on Neon/Supabase) |
| **ORM** | SQLAlchemy | Database connection and query management |
| **Security** | Bcrypt | Password hashing and salt generation |
| **Visualization** | Plotly | Dynamic charts and graphs |

## ⚙️ Local Installation & Setup

Follow these steps to run the application locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/employee-management-system.git](https://github.com/yourusername/employee-management-system.git)
cd employee-management-system 
```

### 2. Install Dependencies
```Bash
pip install -r requirements.txt
```

### 3. Configure Database Secrets
```Bash
Create a folder named .streamlit in the root directory. Inside, create a file named secrets.toml:

# .streamlit/secrets.toml
[database]
url = "postgresql://user:password@host:port/dbname"
(Replace the URL with your actual PostgreSQL connection string).
```
### 4. Run the Application
```Bash
streamlit run app.py
```
## 🗄️ Database Schema
#### Run the following SQL commands in your PostgreSQL query editor to set up the necessary tables:
```bash
SQL

-- Users Table (Authentication)
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role VARCHAR(20) CHECK (role IN ('Admin', 'Employee')) NOT NULL
);

-- Employees Table (Data)
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    role VARCHAR(50),
    salary NUMERIC(10, 2),
    status VARCHAR(20) DEFAULT 'Active',
    joined_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
## 🌐 Deployment (Streamlit Cloud)
1 Push code to **GitHub**.

2 Log in to **Streamlit Community Cloud**.

3 Click **New App** and select your repository.

4 Go to **Advanced Settings** -> **Secrets** and paste your database URL:
```bash
[database]
url = "postgresql://..."
```
5 Click Deploy!

## 🔮 Future Enhancements

* [ ] **PDF Export:** Generate monthly payroll reports.

* [ ] **Profile Pictures:** Allow image uploads for employees (Stored in AWS S3).

* [ ] **Email Notifications:** Auto-email on new employee registration.

* [ ] **AI Assistant:** Chatbot to query database using natural language.

## 🌐 Live Demo

🚀 **Live Application:**  
👉 https://employee-management-system.streamlit.app


### Developed by [Tanmay Nagare]
