from database import connect

def send_message(sender, receiver, message):
    conn = connect()
    c = conn.cursor()

    c.execute("INSERT INTO messages (sender, receiver, message) VALUES (?, ?, ?)",
              (sender, receiver, message))

    conn.commit()
    conn.close()

def get_global():
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT sender, message FROM messages WHERE receiver='global'")
    return c.fetchall()