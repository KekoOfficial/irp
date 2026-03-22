from database import connect
from security import hash_password

def create_user(name, password):
    conn = connect()
    c = conn.cursor()

    hashed = hash_password(password)

    c.execute("INSERT INTO users (name, password, role) VALUES (?, ?, ?)",
              (name, hashed, "user"))

    conn.commit()
    conn.close()