import pyautogui
from pynput.keyboard import *
import keyboard
import time

#  ======== settings ========
delay = 3  # in seconds
resume_key = Key.f7
pause_key = Key.f8
#  ==========================

pause = True

def on_press(key):
    global pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")

def display_controls():
    print("// D2TurnSkipper for Disciples 2")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F7 = Start\Resume")
    print("\t F8 = Pause")
    print("-----------------------------------------------------")
    print('Press F7 to start ...')

def skip_turn():
    pyautogui.click(pyautogui.position())
    time.sleep(0.3)
    pyautogui.click(pyautogui.position())
    time.sleep(0.3)
    keyboard.press('i')
    keyboard.press('enter')
    time.sleep(0.3)
    keyboard.press('esc')
    keyboard.press('space')

def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    pyautogui.PAUSE = delay
    while True:
        if not pause:
            skip_turn()
    lis.stop()


if __name__ == "__main__":
    main()
