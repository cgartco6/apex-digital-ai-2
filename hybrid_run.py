from hybrid.admin.dashboard import Dashboard
from hybrid.governance.override import status

if __name__ == "__main__":
    print("🏢 APEX HYBRID CORPORATION")
    print("Dashboard:", Dashboard().stats())
    print("Override Active:", status())
