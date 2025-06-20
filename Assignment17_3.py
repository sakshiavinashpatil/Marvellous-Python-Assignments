import schedule
import time

def motivate():
    print("Do Coding..!")

schedule.every(30).minutes.do(motivate)

while True:
    schedule.run_pending()
    time.sleep(1)