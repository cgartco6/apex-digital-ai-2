from database.mysql import get_db_connection

def log_action(user_id, agency_id, action, details=""):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO audit_logs (user_id, agency_id, action, details)
        VALUES (%s,%s,%s,%s)
    """, (user_id, agency_id, action, details))
    conn.commit()
    conn.close()
