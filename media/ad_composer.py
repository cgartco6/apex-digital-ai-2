from media.image_creator import create as img
from media.video_creator import create as vid

def compose(offer):
    return {
        "poster": img(f"Ad poster for {offer}"),
        "short": vid(f"15s vertical ad for {offer}")
    }
