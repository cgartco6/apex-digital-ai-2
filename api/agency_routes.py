from flask import Blueprint, request, jsonify
from database.mysql import get_db_connection

agency_api = Blueprint("agency_api", __name__)

@agency_api.route("/create", methods=["POST"])
def create_agency():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO agencies (name, domain, logo, primary_color)
        VALUES (%s,%s,%s,%s)
    """, (
        data["name"],
        data["domain"],
        data.get("logo"),
        data.get("color", "#0F9D58")
    ))
    conn.commit()
    conn.close()
    return jsonify({"status": "agency_created"})

@agency_api.route("/list")
def list_agencies():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM agencies")
    agencies = cur.fetchall()
    conn.close()
    return jsonify(agencies)
