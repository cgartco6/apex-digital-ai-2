OVERRIDE = False

def enable():
    global OVERRIDE
    OVERRIDE = True

def status():
    return OVERRIDE
