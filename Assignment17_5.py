import schedule
import time
from datetime import datetime

def log_time():
    with open("Marvellous.txt", "a") as f:
        f.write(f"{datetime.now()}\n")

schedule.every(5).minutes.do(log_time)

while True:
    schedule.run_pending()
    time.sleep(1)