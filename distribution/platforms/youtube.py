def publish(content, creds=None):
    return {"youtube": "queued" if not creds else "attempted"}
