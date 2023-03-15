#!/usr/bin/python3

import pystray
import os
from PIL import Image, ImageDraw

dir = os.path.dirname(os.path.abspath(__file__))
icon = pystray.Icon("Some Tray Item")
icon.title = "Battery Conservation Mode"

f = open("/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode", "r")
raw_state = f.readline(1)

state = True if raw_state == '1' else False

def set_conservation_mode(mode):
    if mode == True:
        os.system("echo 1 | pkexec tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004\\:00/conservation_mode")
    elif mode == False:
        os.system("echo 0 | pkexec tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004\\:00/conservation_mode")

def on_click(icon, item):
    global state
    state = not item.checked
    print(state)
    set_conservation_mode(state)

def create_image():
    image = Image.open(dir + "/icon.png")
    return image

icon.icon = create_image()
icon.menu = pystray.Menu(
    pystray.MenuItem(
        "Battery Conservation Mode",
        on_click,
        checked=lambda item: state)
    )

icon.run()
