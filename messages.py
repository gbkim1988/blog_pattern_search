#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      YES24
#
# Created:     10-04-2017
# Copyright:   (c) YES24 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import datetime as logtime
from enum import Enum

class LogLevel(Enum):
    ERROR = 1
    INFO = 2
    WARNING = 3
    DEBUG = 4


class MessageBlock(object):
    def __init__(self, who, msg, level=LogLevel.DEBUG):
        self._who = who
        self._when = self.log_time()
        self._msg = msg
        self._lvl = level

    def log_time(self):
        nw = logtime.datetime.now()
        return nw.isoformat()

    def get(self):
        """ return message block  """
        return {
            'who':self._who,
            'when':self._when,
            'msg':self._msg,
            'level': self._lvl
        }

def main():
    import sys
    print (sys.version)
    bmsg = MessageBlock('me','hello me')
    pass

if __name__ == '__main__':
    main()
