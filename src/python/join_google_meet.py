import time
from time import sleep
import pyautogui
import webbrowser

# Prerequisites:
# 1. Install firefox browser
# 2. In firefox, log in to your google account
# 3. Allow camera and microphone access in Google meet

link = "https://meet.google.com/hna-cgyo-urc"

time = "hr:min"


def join_firefox():
    # Register Firefox with its path
    firefox_path = '/Applications/Firefox.app/Contents/MacOS/firefox'
    # webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
    webbrowser.register('firefox', None, webbrowser.GenericBrowser(firefox_path))

    # Get the registered browser and open a URL
    firefox = webbrowser.get('firefox')
    firefox.open(link)
    # webbrowser.open_new_tab(link)
    sleep(5)
    # auto.hotkey('ctrl', 'd')
    # auto.hotkey('ctrl', 'e')
    pyautogui.hotkey('command', 'd')
    pyautogui.hotkey('command', 'e')
    pyautogui.click(1270, 560)

join_firefox()