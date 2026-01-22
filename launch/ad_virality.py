from random import choice

PROMOTION_TYPES = [
    "short_vertical",   # 15–30s TikTok/Instagram Reel style
    "carousel_post",    # Facebook/Instagram multi-image
    "story_post",       # ephemeral content
    "interactive_poll", # engagement-driven
    "music_overlay",    # add trending audio
]

def score_ad(ad_content):
    # Simple heuristic: length, format, media type
    score = 50
    if "video" in ad_content:
        score += 20
    if "voice" in ad_content:
        score += 10
    if "poster" in ad_content:
        score += 5
    return score

def pick_promotion_type(ad_content):
    return choice(PROMOTION_TYPES)
