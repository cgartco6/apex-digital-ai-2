def publish(content, creds=None):
    return {"tiktok": "queued" if not creds else "attempted"}
