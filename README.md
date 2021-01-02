# `RickrollDetection`
Detects rick rolls. I'm bored.


### Doesn't just check links, because people are getting more creative. Actually grabs audio off the page and compares it with a rickroll.

## Installing
- Tested on **Python 3.8**.

Just clone the repo. Run `pip install -r requirements.txt` to grab the required libs. The entry file is `main.py`. Run `py main.py` or `python main.py` on Windows.

**Note:** Because of the way this program interacts with `youtube-dl` and due to the internals of `youtube-dl`, after installing the libs, you should go to your Python install location, go to `Lib/site-packages/youtube_dl/`, and edit `__init__.py`. In the `_real_main` function, on line `469`, change the `sys.exit()` call into `return retcode`.

**Another note:** since I may occasionally add new features/fixes to this code, please, if possible, use `git` to pull this repo instead of downloading a .zip. Then run `update.bat` periodically to receive updates.

| :warning: Warning: Not gonna work on Linux. |
|---|

## Usage:
Give it a youtube link. *Magic!*
