import pyautogui
from pynput.keyboard import *
import keyboard
import time
import psutil

#  ======== settings ========
delay = 4  # in seconds
resume_key = Key.f7
pause_key = Key.f8
#  ==========================

pause = True
auto_pause_printed = False

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
    time.sleep(0.5)
    pyautogui.click(pyautogui.position())
    time.sleep(0.5)
    keyboard.press('i')
    time.sleep(0.3)
    keyboard.press('enter')
    time.sleep(1)
    keyboard.press('esc')
    time.sleep(0.1)
    keyboard.press('space')

def main():
    global auto_pause_printed

    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    pyautogui.PAUSE = delay
    while True:
        dis2_processes = len(list(filter(lambda x: str(x.name()).lower() == 'discipl2.exe', psutil.process_iter())))
        if not pause and dis2_processes > 0:
            skip_turn()
            auto_pause_printed = False
        elif dis2_processes == 0 and not auto_pause_printed and not pause:
            print('[Info]: Game is not running, so')
            auto_pause_printed = True
            keyboard.press('f8')
    lis.stop()


if __name__ == "__main__":
    main()
