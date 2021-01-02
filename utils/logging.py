#  Copyright (c) 2021 by Frank Huang. You may edit this code and distribute the software freely.
from termcolor import colored
import colorama
import dotenv
import os

colorama.init()
dotenv.load_dotenv('../.env')

verb = os.getenv('VERBOSE')


def write(src, msg, _v: bool = False):
    if _v:
        if verb:
            print(colored('[' + src + ']' + ' ', color='cyan') + colored(msg, color='yellow'))
    else:
        print(colored('[' + src + ']' + ' ', color='cyan') + msg)
