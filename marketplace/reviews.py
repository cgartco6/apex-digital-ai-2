from database.mysql import get_db_connection

def add_review(service_id, user_id, rating, review_text):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO marketplace_reviews (service_id, user_id, rating, review)
        VALUES (%s,%s,%s,%s)
    """, (service_id, user_id, rating, review_text))
    conn.commit()
    conn.close()

def list_reviews(service_id):
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM marketplace_reviews WHERE service_id=%s", (service_id,))
    reviews = cur.fetchall()
    conn.close()
    return reviews
