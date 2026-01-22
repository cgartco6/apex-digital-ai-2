from media.ad_composer import compose
from distribution.scheduler import run
from revenue.tracker import log

if __name__ == "__main__":
    ad = compose("Apex AI Service")
    results = run(ad)
    log(0, "ads")  # revenue updates come from real gateways
    print("LIVE LOOP:", results)
