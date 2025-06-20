import schedule
import time
from datetime import datetime

def show_time():
    print("Current Time:", datetime.now())

schedule.every(1).minutes.do(show_time)

while True:
    schedule.run_pending()
    time.sleep(1)