import psutil
import sys
import os
from datetime import datetime

def log_processes_to_file(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = os.path.join(directory, "process_log.txt")
    with open(filename, 'w') as f:
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            line = f"Name: {proc.info['name']}, PID: {proc.info['pid']}, User: {proc.info['username']}\n"
            f.write(line)
    print(f"Process log saved to: {filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python ProcInfoLog.py <directory>")
        return
    log_processes_to_file(sys.argv[1])

if __name__ == "__main__":
    main()