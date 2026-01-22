#!/bin/bash
echo "Installing Apex Digital AI-2 full stack..."

# 1. Install Python 3.11 if needed
sudo apt update && sudo apt install -y python3 python3-venv python3-pip

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Upgrade pip
python3 -m pip install --upgrade pip

# 4. Install dependencies
pip install -r requirements.txt fastapi uvicorn mysql-connector-python

# 5. Setup database (SQLite fallback if MySQL unavailable)
python3 database/mysql.py

# 6. Run initial migrations
python3 production/migrations/migrate.py

# 7. Verify credentials
python3 launch/launch_checklist.py

echo "Installation complete!"
