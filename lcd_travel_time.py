# https://github.com/the-raspberry-pi-guy/lcd
import drivers
import time
import requests
import schedule
from travel_time import get_travel_times

display = drivers.Lcd()

def display_times():
    times = get_travel_times()
    display.lcd_clear()
    line = 1
    for time in times:
        print(time)
        display.lcd_display_string(time, line)
        line += 1
    print("----------------")

def safe_display_times():
    retries = 0
    while retries < 10:
        try:
            display_times()
            return
        except (requests.ConnectionError, requests.Timeout):
            print("Couldn't get response.")
            print("----------------")

        retries+=1
        time.sleep(5)

    display.lcd_display_string("Failed to connect.", 1)

try:
    safe_display_times()

    schedule.every(10).minutes.do(safe_display_times)

    while True:
        schedule.run_pending()
        time.sleep(60)

except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()