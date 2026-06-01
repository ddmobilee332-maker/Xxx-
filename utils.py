import sys
import time
import os

def clear_screen():
    os.system('clear')

def typing_print(text, delay=0.01):
    """ทำให้ตัวอักษรค่อยๆ พิมพ์ออกมาแบบสมจริง"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_header(title):
    print("="*60)
    print(f" {title} ")
    print("="*60)
  
