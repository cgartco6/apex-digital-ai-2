from cryptography.fernet import Fernet
import os

KEY_PATH = "storage/.secret.key"

def get_key():
    if not os.path.exists(KEY_PATH):
        key = Fernet.generate_key()
        with open(KEY_PATH, "wb") as f:
            f.write(key)
    else:
        key = open(KEY_PATH, "rb").read()
    return key

def encrypt_file(filepath):
    key = get_key()
    fernet = Fernet(key)
    with open(filepath, "rb") as f:
        data = f.read()
    enc = fernet.encrypt(data)
    with open(filepath, "wb") as f:
        f.write(enc)

def decrypt_file(filepath):
    key = get_key()
    fernet = Fernet(key)
    with open(filepath, "rb") as f:
        data = f.read()
    dec = fernet.decrypt(data)
    with open(filepath, "wb") as f:
        f.write(dec)
