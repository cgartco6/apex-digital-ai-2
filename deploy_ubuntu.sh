#!/bin/bash
source venv/bin/activate

echo "Deploying Apex Hybrid Corporation..."

# 1. Run Live Production Hardening loop
python3 live.py

# 2. Run launch for ad creation & autopost
python3 live_launch.py

echo "Deployment complete!"
