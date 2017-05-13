#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      YES24
#
# Created:     13-04-2017
# Copyright:   (c) YES24 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import threading
from messages import MessageBlock as msgblock

class baseObject(threading.Thread):
    def __init__(self, _tsl):
        threading.Thread.__init__(self)
        self._tsl = _tsl
        pass

    def report(self, who, msg):
        self._tsl.put_message_block(msgblock(who, msg))

def main():
    pass

if __name__ == '__main__':
    main()
