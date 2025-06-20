import schedule
import time

def namaskar():
    print("Namaskar...")

schedule.every().day.at("09:00").do(namaskar)

while True:
    schedule.run_pending()
    time.sleep(1)