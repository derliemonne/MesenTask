# MESEN BUTTON

## Prerequisites
1. We only tested it on Windows.
2. You need two computers. (Though it can run on one machine too).
3. Two computers must be connected to one local network I suppose. You can also try to use RadminVPN or other software to emulate local network.
4. It works on Python version 3.11.5.

## Instruction for Windows users:
1. Download the folder and place it somewhere.
2. Create venv, then activate it and install all packages.
```
python -m venv .venv
```
```
.venv\Scripts\Activate.ps1
```
```
python -m pip install -r .\requirements.txt
```
3. On server machine: type `ipconfig` in command prompt, find your ip and insert it into `server_viewer.py` line where `HOST` variable is.
4. On client machine: insert the same ip in `client_sender.py` where `HOST` variable is.
5. Run `server_viewer.py`.
6. Run `client_sender.py`.
7. Server will open a window with empty (black) picture.
8. Client will try to connect to host and if succeded the GUI opens.
9. GUI consist of one element: button. You can press the button. It's all functionality.
10. Server will update image when client presses the button.
11. Enjoy this art.