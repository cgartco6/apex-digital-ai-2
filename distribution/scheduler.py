from distribution.autoposter import post

def run(ad):
    platforms = ["tiktok", "facebook", "instagram", "youtube"]
    return [post(p, ad) for p in platforms]
