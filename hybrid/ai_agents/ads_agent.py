from .file_generator import generate_text_file

def ads_agent(job):
    copy = f"""
AD SET

Primary Text:
{job.get("brief","Grow your business with AI")}

Headline:
AI That Works For You

CTA:
Get Started

Formats:
- Facebook Feed
- Instagram Story
- Google Display
"""
    path = generate_text_file(
        "storage/ads",
        "ad_copy",
        copy,
        "txt"
    )

    return {
        "status": "completed",
        "type": "ads",
        "files": [path]
    }
