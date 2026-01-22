import time

LAST = {}

def allow(key, interval=2):
    now = time.time()
    if key in LAST and now - LAST[key] < interval:
        return False
    LAST[key] = now
    return True
