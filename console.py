#-------------------------------------------------------------------------------
# Name:        Console Thread
# Purpose:
#
# Author:      YES24
#
# Created:     13-04-2017
# Copyright:   (c) YES24 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import multiprocessing
import time
from enum import Enum
from main_thrusters import MainThruster
import sys

class Console:
    def __init__(self):
        self._cmd_queue = multiprocessing.JoinableQueue()
        self._result_queue = multiprocessing.Queue()
        self._mt = MainThruster()
        pass

    def run(self):
        while True:
            #print("q: quit, c: continue, p: pause, s: status")
            cmd = input()
            if cmd == 'q': # quit
                pass
            elif cmd == 'c': # continue
                self._mt.start()
                pass
            elif cmd == 'p': # pause
                pass
            elif cmd == 's': # status
                pass
            elif cmd == 'x': # terminate
                print('bye bye ~ ')
                exit()

class Command(Enum):
    QUIT = 1
    CONT = 2
    PAUS = 3
    STAT = 4

def main():
    cs = Console()
    cs.run()

if __name__ == '__main__':
    main()
