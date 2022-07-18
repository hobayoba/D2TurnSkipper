# D2TurnSkipper
just a small script to skip turns in Disciples 2.
useful if you wanna look at your map on 30+ turn

# Setup
1) install python v3.8+ https://www.python.org/downloads/
2) install the following dependencies using `cmd.exe`: `pip install pyautogui pynput keyboard`
3) clone this repo to `C:\example`

# Run:
1) run your map in Disciples 2 and disable the following options in settings:
- show end-of-turn confirmation message
- show enemy actions
- always show results
2) open `cmd.exe` and run D2TurnSkipper: `python C:\example\AutoTurnSkipper.py`
3) return to Disciples 2 and press F7
4) press F8 to pause D2TurnSkipper. ATTENTION: always wait while D2TurnSkipper complete clicks. it takes about 5-10 seconds after pressing F8.

# Known issues
- it opens a chat window
  *solution*: ignore this, this's a normal behavior
- from time to time activated D2TurnSkipper opens a settings window in the Game
  *solution*: wait for 5 seconds then it should close a settings windows, otherwise, press `Esc` or change delay [here](https://github.com/hobayoba/D2TurnSkipper/blob/main/AutoTurnSkipper.py#L7) and restart D2TurnSkipper

------
# Thanks
thanks for an idea and for the source code to @isaychris  
https://github.com/isaychris/python-autoclicker

