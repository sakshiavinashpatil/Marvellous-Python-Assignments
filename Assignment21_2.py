import psutil
import sys

def display_process_by_name(proc_name):
    found = False
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if proc.info['name'] and proc_name.lower() in proc.info['name'].lower():
            print(f"Name: {proc.info['name']}, PID: {proc.info['pid']}, User: {proc.info['username']}")
            found = True
    if not found:
        print(f"No process named '{proc_name}' is running.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python ProcInfo.py <process_name>")
        return
    display_process_by_name(sys.argv[1])

if __name__ == "__main__":
    main()