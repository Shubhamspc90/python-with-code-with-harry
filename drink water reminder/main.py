import time
from plyer import notification

while True:
    print("Plaease sip some water")
    notification.notify(title="Please Drink some water.",
                 message="You need to drink some water",)
    time.sleep(20)