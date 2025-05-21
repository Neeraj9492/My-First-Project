import time
from plyer import notification  #install plyer
while True:
    print("Time for drink water")
    notification.notify(title="Drink Water",message="You need to drink some water",)
    time.sleep(60*60)