from plyer import notification
from time import sleep
import requests

data = requests.get("https://api.adviceslip.com/advice")

while True:
    if data.status_code == 200:
        notification.notify(title="Adive",message=data.json()["slip"]["advice"],timeout=10)
        sleep(20)
