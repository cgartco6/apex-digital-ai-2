from database.mysql import get_db_connection

def has_permission(user_id, action):
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT p.action FROM clients c
        JOIN roles r ON c.role_id = r.id
        JOIN permissions p ON p.role_id = r.id
        WHERE c.id=%s
    """, (user_id,))
    allowed = [row["action"] for row in cur.fetchall()]
    conn.close()
    return action in allowed
