import pandas as pd
from sqlalchemy import text
from database.db import get_engine

engine = get_engine()

def get_all():
    return pd.read_sql("SELECT * FROM employees", engine)

def add(name, dept, role, salary, status):
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO employees (name,department,role,salary,status) VALUES (:n,:d,:r,:s,:st)"),
            {"n": name,"d":dept,"r":role,"s":salary,"st":status}
        )
        conn.commit()

def delete(emp_id):
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM employees WHERE id=:i"),{"i":emp_id})
        conn.commit()

def update(emp_id, name, dept, role, salary, status):
    with engine.connect() as conn:
        conn.execute(
            text("""
                UPDATE employees
                SET name=:n,
                    department=:d,
                    role=:r,
                    salary=:s,
                    status=:st
                WHERE id=:i
            """),
            {
                "n": name,
                "d": dept,
                "r": role,
                "s": salary,
                "st": status,
                "i": emp_id
            }
        )
        conn.commit()
