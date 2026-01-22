import os

class Credentials:
    def __init__(self):
        # Social media API keys
        self.tiktok_key = os.getenv("TIKTOK_API_KEY")
        self.instagram_key = os.getenv("INSTAGRAM_API_KEY")
        self.facebook_key = os.getenv("FACEBOOK_API_KEY")
        self.youtube_key = os.getenv("YOUTUBE_API_KEY")
        
        # Payment
        self.payfast_key = os.getenv("PAYFAST_KEY")
        self.stripe_key = os.getenv("STRIPE_KEY")

        # Database
        self.mysql_user = os.getenv("MYSQL_USER")
        self.mysql_pass = os.getenv("MYSQL_PASS")
        self.mysql_db = os.getenv("MYSQL_DB")
