from database import connect
from security import verify

def login(password):
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT name, password FROM users")
    users = c.fetchall()

    for name, hashed in users:
        if verify(password, hashed):
            return name

    return None