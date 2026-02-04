from flask import Blueprint, request, jsonify
from hybrid.ai_pm.project_manager import run_project

creative_api = Blueprint("creative_api", __name__)

@creative_api.route("/request", methods=["POST"])
def creative_request():
    job = request.json
    result = run_project(job)
    return jsonify(result)
