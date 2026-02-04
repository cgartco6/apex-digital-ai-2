from flask import Flask
app = Flask(__name__)

# Import and register all API blueprints
from api.hybrid_routes import hybrid_api
from api.ai_pm_routes import ai_pm_api
from api.billing_routes import billing_api
from api.agency_routes import agency_api
from api.creative_routes import creative_api
from api.marketplace_routes import marketplace_api
from api.growth_routes import growth_api
from api.compliance_routes import compliance_api

app.register_blueprint(hybrid_api, url_prefix="/api")
app.register_blueprint(ai_pm_api, url_prefix="/api/pm")
app.register_blueprint(billing_api, url_prefix="/api/billing")
app.register_blueprint(agency_api, url_prefix="/api/agency")
app.register_blueprint(creative_api, url_prefix="/api/creative")
app.register_blueprint(marketplace_api, url_prefix="/api/marketplace")
app.register_blueprint(growth_api, url_prefix="/api/growth")
app.register_blueprint(compliance_api, url_prefix="/api/compliance")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
