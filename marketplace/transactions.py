from database.mysql import get_db_connection
from agencies.revenue import split_revenue

def record_transaction(service_id, buyer_id, amount, currency="USD"):
    # Fetch agency
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT agency_id FROM marketplace_services WHERE id=%s", (service_id,))
    agency = cur.fetchone()
    platform_share, agency_share = split_revenue(amount).values()

    cur.execute("""
        INSERT INTO marketplace_transactions
        (service_id, buyer_id, amount, currency, platform_fee, agency_share, status)
        VALUES (%s,%s,%s,%s,%s,%s,'completed')
    """, (service_id, buyer_id, amount, currency, platform_share, agency_share))
    conn.commit()
    conn.close()
    return {"platform_fee": platform_share, "agency_share": agency_share}
