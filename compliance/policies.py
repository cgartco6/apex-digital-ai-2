def data_retention_policy():
    return {
        "client_data_days": 365,
        "audit_log_days": 730,
        "delete_on_request": True
    }

def privacy_policy():
    return "Your data is encrypted, anonymized, and never sold. POPIA & GDPR compliant."
