import schedule
import time

def greet():
    print("Jay Ganesh...")

schedule.every(2).seconds.do(greet)

while True:
    schedule.run_pending()
    time.sleep(1)