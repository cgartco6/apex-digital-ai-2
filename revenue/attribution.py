def attribute(clicks, conversions):
    return {"roi": conversions / max(1, clicks)}
