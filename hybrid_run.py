from hybrid.admin.dashboard import Dashboard
from hybrid.governance.override import status
from api.creative_routes import creative_api
from api.compliance_routes import compliance_api
app.register_blueprint(compliance_api, url_prefix="/api/compliance")

app.register_blueprint(creative_api, url_prefix="/api/creative")
if __name__ == "__main__":
    print("🏢 APEX HYBRID CORPORATION")
    print("Dashboard:", Dashboard().stats())
    print("Override Active:", status())
