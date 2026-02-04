def schedule_social_posts(posts):
    for post in posts:
        # integrate with social API (Ayrshare, etc.)
        print(f"Scheduled post: {post['content']} at {post['time']}")

def send_email_campaign(campaign):
    for recipient in campaign["recipients"]:
        print(f"Sending email to {recipient['email']} with subject {campaign['subject']}")
