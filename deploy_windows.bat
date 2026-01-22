@echo off
call venv\Scripts\activate.bat

echo Deploying Apex Hybrid Corporation...

:: Run Live Production Hardening loop
python live.py

:: Run launch with autoposting
python live_launch.py

echo Deployment complete!
pause
