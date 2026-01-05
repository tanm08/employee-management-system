from sqlalchemy import text
from database.db import get_engine
from utils.hash import check_password, hash_password

engine = get_engine()

def login_user(username, password):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT password_hash, role FROM users WHERE username=:u"),
            {"u": username}
        ).fetchone()

    if result and check_password(password, result[0]):
        return True, result[1]
    return False, None

def create_user(username, password, role):
    hp = hash_password(password)
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO users (username,password_hash,role) VALUES (:u,:p,:r)"),
            {"u": username, "p": hp, "r": role}
        )
        conn.commit()
