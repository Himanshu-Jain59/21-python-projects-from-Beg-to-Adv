from cryptography.fernet import Fernet
import json
import os

FILE = "data.json"

# Create key once
if not os.path.exists("key.key"):
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)
else:
    with open("key.key", "rb") as f:
        key = f.read()

cipher = Fernet(key)

# Load saved passwords
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        data = json.load(f)
else:
    data = {}

while True:
    print("\n1. Add password")
    print("2. View password")
    print("3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        site = input("Site: ")
        password = input("Password: ")
        encrypted = cipher.encrypt(password.encode()).decode()
        data[site] = encrypted

        with open(FILE, "w") as f:
            json.dump(data, f)

        print("Saved!")

    elif choice == "2":
        site = input("Site: ")
        if site in data:
            decrypted = cipher.decrypt(data[site].encode()).decode()
            print("Password:", decrypted)
        else:
            print("Not found!")

    elif choice == "3":
        break