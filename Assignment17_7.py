import schedule
import time
from datetime import datetime
import shutil

def backup():
    src = "data.txt"
    dst = "backup_data.txt"
    shutil.copy(src, dst)
    with open("backup_log.txt", "a") as log:
        log.write(f"Backup done at {datetime.now()}\n")

schedule.every().hour.do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)