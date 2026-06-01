# -*- coding: utf-8 -*-
import sys
from config import LOG, VERSION, AUTHOR
from utils import clear_screen, typing_print
from link_tool import run_link_tool
from system_tool import run_system_tool
from access_tool import run_access_tool

def main_menu():
    while True:
        clear_screen()
        # แสดงโลโก้ที่แท้จริงของคุณรุ่นใหญ่
        print(LOG)
        print(f" [ Project Name: รุ่นใหญ่ HUB Tool Suite ]   Version: {VERSION}")
        print(f" [ Created By  : {AUTHOR} ]")
        print("="*60)
        print("  SELECT AVAILABLE TOOLS FROM THE HUB:")
        print("="*60)
        print("  [1] URL LINK DEEP ANALYZER & AUDITOR   (เปิดและแกะรายละเอียดลิงก์)")
        print("  [2] SYSTEM REPAIR & DEFENSE CORE SHIELD (ซ่อมแซมระบบและล้างไวรัส)")
        print("  [3] ACCOUNT PLATFORM CONTROL ACCESSOR   (การเข้าถึงระบบควบคุมบัญชี)")
        print("  [4] EXIT HUB SYSTEM                     (ออกจากระบบ)")
        print("="*60)
        
        choice = input("Enter choice [1-4]: ").strip()
        
        if choice == '1':
            clear_screen()
            run_link_tool()
        elif choice == '2':
            clear_screen()
            run_system_tool()
        elif choice == '3':
            clear_screen()
            run_access_tool()
        elif choice == '4':
            typing_print("\n[*] Shutting down รุ่นใหญ่ HUB Session... Goodbye!")
            sys.exit()
        else:
            print("[!] Invalid option! Please select 1-4.")
            import time
            time.sleep(1.5)

if __name__ == "__main__":
    main_menu()
  
