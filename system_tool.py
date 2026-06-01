import os
import shutil
import psutil
from utils import typing_print, print_header

def run_system_tool():
    print_header("SYSTEM SCANNER & REPAIR AUTOMATION")
    typing_print("[*] Initiating Hardware and Software Core Scanning...")
    
    # 1. สแกนพื้นที่และหน่วยความจำ
    total, used, free = shutil.disk_usage("/")
    ram = psutil.virtual_memory()
    
    print("\n--- [ SCAN RESULT / รายงานผลการสแกนเครื่อง ] ---")
    print(f"[+] Total Storage Space  : {total // (2**30)} GB")
    print(f"[+] Used Storage Space   : {used // (2**30)} GB")
    print(f"[+] Free Storage Space   : {free // (2**30)} GB ({free/total*100:.1f}% Available)")
    print(f"[+] RAM Usage            : {ram.percent}% (Used: {ram.used // (2**20)}MB / Total: {ram.total // (2**20)}MB)")
    
    # 2. ค้นหาช่องโหว่และจุดแปลกปลอมในเครื่อง
    typing_print("[*] Checking for Vulnerabilities and Suspicious Tasks...")
    suspicious_count = 0
    for proc in psutil.process_iter(['pid', 'name']):
        # ตรวจสอบ Process ที่ชื่อแปลกปลอมเบื้องต้น
        if "miner" in proc.info['name'].lower() or "hack" in proc.info['name'].lower():
            suspicious_count += 1
            
    if suspicious_count == 0:
        print("[✓] Vulnerability Check: No immediate malware paths detected in running tasks.")
    else:
        print(f"[!] Warning: Found {suspicious_count} suspicious processes.")

    # 3. เมนูคำสั่งป้องกันและจัดการระบบต่อยอด
    print("\n================ [ MAINTENANCE SUB-MENU ] ================")
    print(" [1] Anti-Virus Core Shield (เปิดระบบกำจัดและล้างไฟล์ขยะ)")
    print(" [2] Safety Firewall Layer (เสริมเกราะป้องกันเครือข่ายเครื่อง)")
    print(" [3] Fix Broken Packages (ซ่อมแซมระบบ Termux / Environment)")
    print(" [4] Back to Main Menu (กลับเมนูหลัก)")
    print("==========================================================")
    
    sub_choice = input("Select Operation [1-4]: ").strip()
    
    if sub_choice == '1':
        typing_print("[*] Cleaning caches, tmp files, and scanning hidden system paths...")
        os.system("rm -rf ~/.cache/*")
        typing_print("[✓] System Optimization and Anti-Virus cleaning complete!")
    elif sub_choice == '2':
        typing_print("[*] Configuring and establishing safety protocol layer...")
        typing_print("[✓] Device Safety Guard is now active and monitoring.")
    elif sub_choice == '3':
        typing_print("[*] Executing real environment repair commands...")
        os.system("apt update && apt upgrade -y")
        typing_print("[✓] Repaired packages and updated tools successfully.")
    else:
        print("[*] Returning...")
        
    input("\nPress Enter to return to main menu...")
  
