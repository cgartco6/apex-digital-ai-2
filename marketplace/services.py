from database.mysql import get_db_connection

def list_services():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM marketplace_services")
    services = cur.fetchall()
    conn.close()
    return services

def create_service(agency_id, name, category, description, price, currency="USD"):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO marketplace_services (agency_id, name, category, description, price, currency)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (agency_id, name, category, description, price, currency))
    conn.commit()
    conn.close()
