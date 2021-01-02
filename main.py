# This is a Rickroll blocker. I'm writing this because I'm sick of people giving me rickroll links. If I can't afford
# to be trolled, I will let a machine listen to all videos on a page to see if they might be rickrolls. :D

from meldetect import isRickRoll
from getvid import getvid
from utils.logging import write
import sys
import os
import librosa.display

if __name__ == '__main__':
    url = input("URL: ")
    getvid(url)
    os.chdir('temp')
    for path in os.listdir('.'):
        _path = os.path.abspath(path)
        res = isRickRoll(_path)

        if res:
            print("isRickRoll returned True")
            os.system('rd /s /q .') # Clean dir
            sys.exit(0)


        os.system('pause')
    print("Seems safe")

    os.system('rd /s /q .')

