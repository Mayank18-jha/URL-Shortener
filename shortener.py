import hashlib
import json
import os
DATA_DIR = "Outputs"
DATA_FILE = os.path.join(DATA_DIR, "urls.json")
os.makedirs(DATA_DIR, exist_ok=True)

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        url_db = json.load(f)
else:
    url_db = {}
def shorten_url(long_url):
    hash_object = hashlib.md5(long_url.encode())
    short_code = hash_object.hexdigest()[:6]
    
    if short_code not in url_db:
        url_db[short_code] = long_url
        save_data()
    return short_code

def retrieve_url(short_code):
    return url_db.get(short_code, "URL not found")
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(url_db, f, indent = 4)
def menu():
    while True:
        print("""
              URL SHORTENER:
              1. Shorten URL
              2. Retrieve URL
              3. Exit
              """)
        choice = input("Enter choice: ")
        if choice == "1":
            long_url = input("Enter long URL: ")
            short_code = shorten_url(long_url)
            print(f"Short URL code: {short_code}")
            
        elif choice == "2":
            code = input("Enter short code: ")
            print("Original URL:", retrieve_url(code))
        elif choice == "3":
            print("Exiting")
            break
        else:
            print("Inavalid Option")
            
menu()