def publish(content, creds=None):
    return {"instagram": "queued" if not creds else "attempted"}
