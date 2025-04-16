import requests
import time
import os
from datetime import datetime

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ascii_banner():
    print(r"""
     █████╗ ██╗   ██╗████████╗ ██████╗ ██╗    ██╗██╗███████╗██╗
    ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██║    ██║██║██╔════╝██║
    ███████║██║   ██║   ██║   ██║   ██║██║ █╗ ██║██║█████╗  ██║
    ██╔══██║██║   ██║   ██║   ██║   ██║██║███╗██║██║██╔══╝  ██║
    ██║  ██║╚██████╔╝   ██║   ╚██████╔╝╚███╔███╔╝██║██╗     ██╗
    ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝  ╚══╝╚══╝ ╚═╝╚═╚     ╚═╝
                        WiFi Auto-Login Utility
    """)

def login():
    payload = {
        "username": "user_id", # Enter your user_ID
        "password": "password" # Enter your Password
    }
    login_url = "http://geckhagaria.com/login"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    print(f"\n🔐 Sending login request to: {login_url}")
    with requests.Session() as session:
        try:
            response = session.post(login_url, data=payload, headers=headers, timeout=10)
            if response.ok:
                print("✅ Login request sent successfully")
            else:
                print("❌ Login failed with status code:", response.status_code)
        except requests.RequestException as e:
            print("❌ Login request error! \n Doing some Magic....🪄")

def main():
    clear()
    ascii_banner()
    login_url = "http://geckhagaria.com/login"
    print(f"\n🌐 Monitoring connection. Auto-login to: {login_url}\n")

    # check_count = 0
    while True:
        try:
            check = requests.get("https://www.google.com", timeout=5)
            timestamp = datetime.now().strftime("%H:%M:%S")
            if check.status_code == 200:
                # check_count += 1
                print(f"[{timestamp}] 🌐 Internet connected: ✅")
                time.sleep(2)
            else:
                print(f"[{timestamp}] ⚠️ Unexpected status. Trying login...")
                login()
                time.sleep(5)
        except requests.RequestException:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] 🚫 No internet! Trying login...")
            login()
            time.sleep(5)

if __name__ == "__main__":
    main()
