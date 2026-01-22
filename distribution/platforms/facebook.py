def publish(content, creds=None):
    return {"facebook": "queued" if not creds else "attempted"}
