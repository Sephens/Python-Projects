from socket import timeout
import time
from turtle import title
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Hey!!",
            message = "How are you",
            timeout = 20
        )
        time.sleep(3600)
