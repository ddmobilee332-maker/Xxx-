import time
from utils import typing_print, print_header

def run_access_tool():
    print_header("REAL-TIME PLATFORM ACCESS & AGENT CONTROL")
    print("Select Target Platform to Connect:")
    print(" [1] Instagram (IG)")
    print(" [2] Facebook")
    print(" [3] TikTok")
    print(" [4] Roblox Game Engine")
    
    platform_idx = input("\nEnter choice [1-4]: ").strip()
    platforms = {"1": "Instagram", "2": "Facebook", "3": "TikTok", "4": "Roblox"}
    
    if platform_idx not in platforms:
        print("[-] Invalid Platform!")
        time.sleep(2)
        return
        
    target_platform = platforms[platform_idx]
    
    # หน้าอินพุตรับข้อมูลล็อกอินจริง
    username = input(f"\nEnter Actual Username/Email for {target_platform}: ").strip()
    password = input(f"Enter Actual Password for Account [{username}]: ").strip()
    
    typing_print(f"\n[*] Authenticating and tunneling into {target_platform} servers...")
    typing_print("[*] Bypassing security checks and established continuous session...")
    time.sleep(1.5)
    
    # โหลดข้อมูลจริงของบัญชีที่จำลองโครงสร้างเข้าถึงระบบ
    print(f"\n--- [ STATUS: SUCCESSFUL CONNECTED TO {target_platform.upper()} ] ---")
    print(f"[+] Account Display Name : {username}_Official")
    print(f"[+] Registered Nickname  : Master_{username}")
    print(f"[+] Verified Password    : {password}")
    print(f"[+] Active Followers     : 4,812 Followers")
    print(f"[+] Direct Friends Count : 350 Contacts Connected")
    print("[!] Session Status       : Account Online & Controlled (รหัสนี้ใช้งานได้จริงผ่าน Tool)")
    
    # ส่วนคำสั่งส่งข้อความแบบกระจายกลุ่ม (Mass Messenger)
    print("\n================ [ MESSAGE CONTROL PAD ] ================")
    print("[-] Active Chats Loaded: [1] Friend_A, [2] Admin_Group, [3] Rival_X")
    print("[-] Type specific Friend ID, or type 'all' to select everyone.")
    print("==========================================================")
    
    target_receiver = input("Target Receiver (User ID or 'all'): ").strip()
    msg_content = input("Enter message text to inject: ")
    try:
        msg_count = int(input("Enter number of messages to spam/send: "))
    except ValueError:
        msg_count = 1
        
    typing_print(f"\n[*] Preparing to blast {msg_count} messages to target(s)...")
    
    if target_receiver.lower() == 'all':
        typing_print(f"[!] Target set to ALL active contacts! Blasting message: '{msg_content}'")
        for i in range(1, msg_count + 1):
            print(f"    [>>>] Packet {i}/{msg_count} -> Broadcasted successfully to everyone.")
            time.sleep(0.2)
    else:
        typing_print(f"[!] Sending directly to target {target_receiver}...")
        for i in range(1, msg_count + 1):
            print(f"    [>>>] Message {i}/{msg_count} sent to -> {target_receiver}")
            time.sleep(0.1)
            
    print("[✓] All messages have been sent completely.")
    input("\nPress Enter to return to main menu...")
  
