from flask import Blueprint, jsonify
from growth_ai import lead_gen, sales_agent, upsell_engine, marketing_automation, analytics

growth_api = Blueprint("growth_api", __name__)

@growth_api.route("/run_growth_cycle")
def run_growth_cycle():
    leads = lead_gen.generate_leads()
    sales = sales_agent.batch_outreach(leads, ["logo", "website", "video"])
    conversion = analytics.track_conversions(leads, sales)
    return jsonify({
        "leads_generated": leads,
        "sales_outreach": sales,
        "conversion_metrics": conversion
    })
