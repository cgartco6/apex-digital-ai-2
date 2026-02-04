from .file_generator import generate_text_file

def video_agent(job):
    script = f"""
VIDEO SCRIPT

Brand: {job.get("brand","AI Brand")}
Goal: {job.get("goal","Promotion")}

Scene 1:
Hook – problem statement

Scene 2:
Solution – AI-powered service

Scene 3:
CTA – Start Today
"""
    path = generate_text_file(
        "storage/videos",
        job.get("brand","video"),
        script,
        "txt"
    )

    return {
        "status": "completed",
        "type": "video",
        "files": [path],
        "note": "Script & storyboard ready for rendering"
  }
