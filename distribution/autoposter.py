def post(platform, content):
    # Queues post; platform adapter decides based on credentials
    return {"platform": platform, "queued": True, "content": content}
