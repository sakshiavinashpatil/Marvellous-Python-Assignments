import psutil

def display_all_processes():
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print(f"Name: {proc.info['name']}, PID: {proc.info['pid']}, User: {proc.info['username']}")

def main():
    display_all_processes()

if __name__ == "__main__":
    main()