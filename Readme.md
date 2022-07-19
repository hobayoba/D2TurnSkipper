# D2TurnSkipper
just a small script to automate turns skipping in Disciples 2.
useful for cases when you wanna test what happen on your map on 30+ turn.

# Setup
1) install python v3.8+ https://www.python.org/downloads/
2) install the following dependencies using `cmd.exe`: `pip install pyautogui pynput keyboard psutil`
3) clone this repo or just save the [*AutoTurnSkipper.py*](https://raw.githubusercontent.com/hobayoba/D2TurnSkipper/main/AutoTurnSkipper.py) file to `C:\example`

# Run:
1) open `cmd.exe` and run *D2TurnSkipper*: `python C:\example\AutoTurnSkipper.py`
2) run Disciples 2 and increase movement speed and scrolling speed in options, also, disable the following options in settings:
- Confirm end of turn
- Scrolling between actions
- Always show turn summary  
3) start\load your map in single mode or in hotseat mode
4) press F7 to skip turns automatically
5) press F8 to pause turns skipping.  
  ATTENTION: always wait while D2TurnSkipper complete its actions. it takes about 5 seconds (based on this [value](https://github.com/hobayoba/D2TurnSkipper/blob/main/AutoTurnSkipper.py#L8)) every time when F8 key was pressed.

# Known issues
- it opens a chat in the game  
  *solution*: ignore this, it's a normal behavior because this script emulates mouse clicks and keystrokes.   
- from time to time activated D2TurnSkipper opens settings in the game  
  *solution*: wait for 5 seconds then it should close settings automatically, otherwise, press `Esc`  

------
# Thanks
Many thanks for an idea and for the source code to [@isaychris](https://github.com/isaychris)
https://github.com/isaychris/python-autoclicker

