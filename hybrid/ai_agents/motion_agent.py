from .file_generator import generate_text_file

def motion_agent(job):
    svg = f"""
<svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" fill="#000"/>
  <text x="200" y="100" fill="#0F9D58" font-size="28"
        text-anchor="middle">
    {job.get("brand","AI MOTION")}
  </text>
</svg>
"""
    path = generate_text_file(
        "storage/motion",
        "motion_graphic",
        svg,
        "svg"
    )

    return {
        "status": "completed",
        "type": "motion",
        "files": [path]
    }
