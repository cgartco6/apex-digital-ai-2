---

# ⚡ 3. `setup_installer.py`

```python
import subprocess, os

def install():
    print("Installing Apex Digital AI 2.0...")
    subprocess.run("pip install -r requirements.txt", shell=True)
    os.makedirs("storage/videos", exist_ok=True)
    os.makedirs("storage/ads", exist_ok=True)
    os.makedirs("storage/motion", exist_ok=True)
    print("Installation complete!")

if __name__ == "__main__":
    install()
