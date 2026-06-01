import os
import requests
from bs4 import BeautifulSoup
from utils import typing_print, print_header

def run_link_tool():
    print_header("URL ADVANCED ANALYZER & DOWNLOADER")
    url = input("Enter Target URL Link: ").strip()
    
    if not url.startswith("http"):
        url = "https://" + url

    typing_print("\n[*] Fetching and Analyzing Digital Link Data Deeply...")
    
    try:
        # ส่ง Request ตรวจสอบรายละเอียดเชิงลึก
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers, timeout=10)
        
        print("\n--- [ LINK DETAILS INFO ] ---")
        print(f"[+] Target URL     : {url}")
        print(f"[+] HTTP Status    : {response.status_code} (OK)" if response.status_code == 200 else f"[+] Status: {response.status_code}")
        print(f"[+] Server Type    : {response.headers.get('Server', 'Unknown')}")
        print(f"[+] Content-Type   : {response.headers.get('Content-Type', 'Unknown')}")
        print(f"[+] Content Length : {len(response.content)} bytes")
        
        # ค้นหา Metadata และตรวจเช็คบอต/ดิสคอร์ด/เซิร์ฟเวอร์เบื้องต้น
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No Title Found"
        print(f"[+] Page Title     : {title.strip()}")
        
        if "discord.gg" in url or "discord.com/invite" in url:
            typing_print("[!] Discord Invite Link Detected! Parsing Server Status...")
            # ดึงข้อมูล API Discord เบื้องต้นเพื่อดูจำนวนสมาชิก
            invite_code = url.split('/')[-1]
            api_url = f"https://discord.com/api/v9/invites/{invite_code}?with_counts=true"
            res = requests.get(api_url).json()
            if 'guild' in res:
                print(f"    - Server Name    : {res['guild'].get('name')}")
                print(f"    - Total Members  : {res.get('approximate_member_count')}")
                print(f"    - Active Online  : {res.get('approximate_presence_count')}")

        # ฟังก์ชันตรวจสอบสื่อและดาวน์โหลดไฟล์เสียง
        is_media = any(ext in url.lower() for ext in ['.mp3', '.mp4', '.wav', '.ogg', 'youtube', 'video', 'stream'])
        
        if is_media or "audio" in response.headers.get('Content-Type', ''):
            print("\n[!] Media stream/audio content detected in this link!")
            choice = input("Do you want to download this audio? (y/n): ").strip().lower()
            
            if choice == 'y':
                file_name = input("Enter your custom name for MP3 file: ").strip()
                if not file_name.endswith('.mp3'):
                    file_name += '.mp3'
                
                typing_print(f"[*] Downloading and converting to {file_name}...")
                
                # โค้ดดาวน์โหลดและเซฟลงเครื่องจริง
                with open(file_name, 'wb') as f:
                    f.write(response.content)
                typing_print(f"[✓] Success! Downloaded and saved as: {file_name}")
            else:
                print("[-] Download Canceled.")
                
    except Exception as e:
        print(f"[-] Error parsing link: {e}")
    
    input("\nPress Enter to return to main menu...")
              
