from flask import Blueprint, request, jsonify
from marketplace import services, transactions, reviews

marketplace_api = Blueprint("marketplace_api", __name__)

@marketplace_api.route("/services")
def list_all():
    return jsonify(services.list_services())

@marketplace_api.route("/services/create", methods=["POST"])
def create():
    data = request.json
    services.create_service(
        data["agency_id"],
        data["name"],
        data["category"],
        data["description"],
        data["price"],
        data.get("currency","USD")
    )
    return jsonify({"status":"created"})

@marketplace_api.route("/buy", methods=["POST"])
def buy_service():
    data = request.json
    result = transactions.record_transaction(
        data["service_id"],
        data["buyer_id"],
        data["amount"],
        data.get("currency","USD")
    )
    return jsonify(result)

@marketplace_api.route("/reviews/<int:service_id>")
def get_reviews(service_id):
    return jsonify(reviews.list_reviews(service_id))

@marketplace_api.route("/reviews/add", methods=["POST"])
def add_review_route():
    data = request.json
    reviews.add_review(data["service_id"], data["user_id"], data["rating"], data["review"])
    return jsonify({"status":"review_added"})
