import sqlite3
from contextlib import closing
from config import DB_PATH

def get_conn():
    return sqlite3.connect(DB_PATH)

def fetch_all_users():
    with closing(get_conn()) as conn:
         cursor = conn.cursor()
         cursor.execute("SELECT id ,name ,email FROM users")  
         data= cursor.fetchall()
         conn.close()

   

    return data

def fetch_user_by_id(user_id):
    with closing(get_conn()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id ,name ,email FROM users WHERE id = ?", (user_id,))
        data = cursor.fetchone()
        
        
        return data

def insert_user(name, email, password):
    with closing(get_conn()) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                       (name, email, password))
        conn.commit()

def update_user_data(user_id, name=None, email=None):
    with closing(get_conn()) as conn:
        cursor = conn.cursor()
        fields = []
        params = []
        if name:
            fields.append("name = ?")
            params.append(name)
        if email:
            fields.append("email = ?")
            params.append(email)
        params.append(user_id)
        sql = f"UPDATE users SET {', '.join(fields)} WHERE id = ?"
        cursor.execute(sql, tuple(params))
        conn.commit()

def delete_user_by_id(user_id):
    with closing(get_conn()) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()

def search_users_by_name(name):
    with closing(get_conn()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id ,name ,email FROM users WHERE name LIKE ?", (f"%{name}%",))
        return cursor.fetchall()

def validate_user_credentials(email, password):
    with closing(get_conn()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE email = ? AND password = ?", (email, password))
        return cursor.fetchone() is not None

def get_user_by_email(email):
     with closing(get_conn())  as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return cursor.fetchone()
