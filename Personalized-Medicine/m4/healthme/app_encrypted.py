from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
with open("key.key", "wb") as key_file:
    key_file.write(key)

# Enkripsi file
with open("app.py", "rb") as file:
    original = file.read()
fernet = Fernet(key)
encrypted = fernet.encrypt(original)
with open("app_encrypted.py", "wb") as encrypted_file:
    encrypted_file.write(encrypted)

