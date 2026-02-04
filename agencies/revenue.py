PLATFORM_SHARE = 0.3  # 30%
AGENCY_SHARE = 0.7    # 70%

def split_revenue(amount):
    return {
        "platform": round(amount * PLATFORM_SHARE, 2),
        "agency": round(amount * AGENCY_SHARE, 2)
    }
