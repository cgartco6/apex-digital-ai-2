@echo off
echo Installing Apex Digital AI-2 full stack...

:: 1. Create virtual environment
python -m venv venv
call venv\Scripts\activate.bat

:: 2. Upgrade pip
python -m pip install --upgrade pip

:: 3. Install dependencies
pip install -r requirements.txt fastapi uvicorn mysql-connector-python

:: 4. Setup database (SQLite fallback)
python database/mysql.py

:: 5. Run initial migrations
python production/migrations/migrate.py

:: 6. Verify credentials
python launch/launch_checklist.py

echo Installation complete!
pause
