from launch.credentials import Credentials

class LaunchChecklist:
    def __init__(self):
        self.credentials = Credentials()

    def verify(self):
        missing = []
        for key, val in vars(self.credentials).items():
            if not val:
                missing.append(key)
        if missing:
            return False, f"Missing credentials: {', '.join(missing)}"
        return True, "All credentials wired"
