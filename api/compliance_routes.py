from flask import Blueprint, jsonify
from compliance.audit_logs import log_action
from compliance.policies import data_retention_policy, privacy_policy

compliance_api = Blueprint("compliance_api", __name__)

@compliance_api.route("/audit/<int:user_id>/<action>")
def audit(user_id, action):
    log_action(user_id, 0, action)
    return jsonify({"status":"logged"})

@compliance_api.route("/policies")
def policies():
    return jsonify({
        "privacy": privacy_policy(),
        "retention": data_retention_policy()
    })
