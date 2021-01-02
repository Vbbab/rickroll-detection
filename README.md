# `RickrollDetection`
Detects rick rolls. I'm bored.


## Installing
- Tested on **Python 3.8**.

Just clone the repo. Run `pip install -r requirements.txt` to grab the required libs. The entry file is `main.py`. Run `py main.py` or `python main.py` on Windows.

**Note:** Because of the way this program interacts with `youtube-dl` and due to the internals of `youtube-dl`, after installing the libs, you should go to your Python install location, go to `Lib/site-packages/youtube_dl/`, and edit `__init__.py`. In the `_real_main` function, on line `469`, change the `sys.exit()` call into `return retcode`.

| :warning: Warning: Not gonna work on Linux. |
|---|

## Usage:
Give it a youtube link. *Magic!*
