import json
from pathlib import Path

FILE = Path("signals/revenue.json")

def log(amount, source):
    data = []
    if FILE.exists():
        data = json.loads(FILE.read_text())
    data.append({"amount": amount, "source": source})
    FILE.write_text(json.dumps(data, indent=2))
