import subprocess
import time
import pyautogui as pg
import random


subprocess.call(["open", "-a", "WhatsApp"])
time.sleep(10)

messages = ("Hello", "Hey", "Good Morning")

for _ in range(10):
    message = random.choice(messages)
    pg.write(message)
    pg.press("enter")
    time.sleep(random.uniform(1, 3))