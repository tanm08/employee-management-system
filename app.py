import streamlit as st
import plotly.express as px

from auth.auth import login_user, create_user
from crud.employees import get_all, add, delete, update


# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(page_title="EMS Capstone", layout="wide")

# -------------------------------------------------
# Session State Initialization
# -------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.role = None

# -------------------------------------------------
# LOGIN SCREEN
# -------------------------------------------------
if not st.session_state.logged_in:
    st.title("🔐 Employee Management System")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        success, role = login_user(username, password)
        if success:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.session_state.role = role
            st.rerun()
        else:
            st.error("Invalid username or password")

    st.stop()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.title(f"Welcome, {st.session_state.user}")
st.sidebar.caption(f"Role: {st.session_state.role}")

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.role = None
    st.rerun()

# Role-Based Menu
if st.session_state.role == "Admin":
    menu = ["Dashboard", "View Employees", "Add Employee", "Update Employee", "Delete Employee", "Create User"]
else:
    menu = ["Dashboard", "View Employees"]

choice = st.sidebar.radio("Navigation", menu)

# Load data from PostgreSQL
df = get_all()

# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------
if choice == "Dashboard":
    st.title("📊 HR Analytics Dashboard")

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Employees", len(df))
    c2.metric("Total Salary", f"${df['salary'].sum():,.2f}")
    c3.metric("Departments", df['department'].nunique())

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            px.pie(df, names="department", title="Department Distribution"),
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            px.bar(df, x="name", y="salary", color="role", title="Salary Distribution"),
            use_container_width=True
        )

# -------------------------------------------------
# VIEW EMPLOYEES
# -------------------------------------------------
elif choice == "View Employees":
    st.title("📂 Employee Directory")
    st.dataframe(df, use_container_width=True)

# -------------------------------------------------
# ADD EMPLOYEE (Admin only)
# -------------------------------------------------
elif choice == "Add Employee":
    st.title("➕ Add New Employee")

    name = st.text_input("Full Name")
    department = st.selectbox("Department", ["HR", "IT", "Sales", "Finance"])
    role = st.text_input("Role")
    salary = st.number_input("Salary", min_value=0.0)
    status = st.selectbox("Status", ["Active", "Inactive"])

    if st.button("Add Employee"):
        add(name, department, role, salary, status)
        st.success("Employee added successfully")
        st.rerun()

# -------------------------------------------------
# UPDATE EMPLOYEE (Admin only)
# -------------------------------------------------
elif choice == "Update Employee":
    st.title("✏️ Update Employee")

    emp_id = st.number_input("Employee ID", min_value=1)

    emp = df[df["id"] == emp_id]

    if not emp.empty:
        name = st.text_input("Name", emp.iloc[0]["name"])
        dept = st.text_input("Department", emp.iloc[0]["department"])
        role = st.text_input("Role", emp.iloc[0]["role"])
        salary = st.number_input("Salary", value=float(emp.iloc[0]["salary"]))
        status = st.selectbox("Status", ["Active", "Inactive"], index=0 if emp.iloc[0]["status"]=="Active" else 1)

        if st.button("Update Employee"):
            update(emp_id, name, dept, role, salary, status)
            st.success("Employee updated successfully")
            st.rerun()
    else:
        st.warning("Employee ID not found")


# -------------------------------------------------
# DELETE EMPLOYEE (Admin only)
# -------------------------------------------------
elif choice == "Delete Employee":
    st.title("🗑 Delete Employee")

    emp_id = st.number_input("Employee ID", min_value=1)

    if st.button("Delete Employee", type="primary"):
        delete(emp_id)
        st.warning("Employee deleted")
        st.rerun()

# -------------------------------------------------
# CREATE USER (Admin only)
# -------------------------------------------------
elif choice == "Create User":
    st.title("👤 Create System User")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")
    new_role = st.selectbox("Role", ["Admin", "Employee"])

    if st.button("Create User"):
        create_user(new_user, new_pass, new_role)
        st.success("User created successfully")
