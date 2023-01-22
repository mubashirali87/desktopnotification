# desktopnotification
Generating desktop notifications using python
import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title="Alert!!!",
            message="Take a break, relax your eyes for 10 mins",
            timeout=10
        )
        time.sleep(3600)
