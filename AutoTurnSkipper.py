import pyautogui
from pynput.keyboard import *
import keyboard

#  ======== settings ========
delay = 2  # in seconds
resume_key = Key.f7
pause_key = Key.f8
#exit_key = Key.esc
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
#    elif key == exit_key:
#        running = False
#        print("[Exit]")


def display_controls():
    print("// AutoTurnSkipper for Disciples 2 that emulates 2 mouse clicks and one spacebar press to close info dialogs and skip a turn")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F7 = Start\Resume")
    print("\t F8 = Pause")
    print("-----------------------------------------------------")
    print('Press F7 to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.click(pyautogui.position())
            keyboard.press('enter')
            keyboard.press('enter')
            keyboard.press('enter')
            keyboard.press('esc')
            keyboard.press('space')
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()
