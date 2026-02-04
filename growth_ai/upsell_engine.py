def suggest_upsell(client, current_plan):
    if current_plan == "starter":
        return "pro"
    elif current_plan == "pro":
        return "agency"
    return current_plan

def generate_offer(client):
    plan = client.get("plan", "starter")
    upsell = suggest_upsell(client, plan)
    return f"Upgrade {client['name']} from {plan} → {upsell} plan for more AI credits!"
