from .video_agent import video_agent
from .ads_agent import ads_agent
from .motion_agent import motion_agent

elif service == "video":
    return video_agent(job)
elif service == "ads":
    return ads_agent(job)
elif service == "motion":
    return motion_agent(job)
