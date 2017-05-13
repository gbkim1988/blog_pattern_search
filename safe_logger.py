#-------------------------------------------------------------------------------
# Name:        safe logger
# Purpose:     Logging Multiple Thread's message in serial
#
# Author:      YES24
#
# Created:     10-04-2017
# Copyright:   (c) YES24 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''Copyright (c) 2017 gbkim@yes24.com

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.'''

import logging
import logging.handlers
import queue
from messages import MessageBlock as BlockMsg
from messages import LogLevel as lvl
import time

class ThreadSafeLogger(object):
    """ be Referenced from many classes, but it's thread safe, All thread shared the same lock
        after elapse_time, every thread release the lock, if anyone get failed to release or raise error
        all object will be died by Killer Threads, and Check the MainThrusters Status, then
        All Objects will be created again.
    """
    def __init__(self, max_number, path_error='./logs/logger_error.log', path_debug='./logs/logger_debug.log', logger_name1="logger_debug",logger_name2="logger_error"):
        """
        @msg_queue : ThreadSafeLogger queue message blocks received from others
        @lock : ThreadSafeLogger set locks while processing input message blocks
        """
        print ("-- init logger --")
        self._debug = self.init_logger(logger_name1, path_debug)
        self._error = self.init_logger(logger_name2, path_error)
        self._max_queue = max_number
        self._msg_queue = queue.Queue(500)
        self._counter = 0
        self._tickcount = time.time()
        self.CR_POINT_SECS = 2; # every 2 seconds
        pass

    def init_logger(self, name, path, ):
        """ generate logger object for the specific purpose """
        file_max_bytes = 100 * 1024 * 1024
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        fileHandler = logging.handlers.RotatingFileHandler(filename=path, maxBytes=file_max_bytes, backupCount=10)
        streamHandler = logging.StreamHandler()

        formatter = logging.Formatter('%(message)s')

        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.addHandler(streamHandler)

        return logger

    def log_formater(self, _msg):
        form = "[{0}] {1} > {2}"
        msg = ''
        mtmp = _msg.get()
        try:
            msg = form.format(mtmp['who'], mtmp['when'], mtmp['msg'])
            return msg
        except IndexError as e:
            ''' Wrong Message Block Received, Return Nothing '''
            return None

    def tick(self):
        """ every calling put_message_block method,
        tick method is called to check whether or not span time is over the critical
        point
        """
        now = time.time()
        if now - self._tickcount > self.CR_POINT_SECS:
            self._tickcount = time.time()
            return True
        else:
            return False

    def put_message_block(self, _msg):
        """ put message blocks in queue
        _msg = {
            'who' : 'fetcher001',
            'when' : '2017-03-04 blah blah',
            'msg' : 'some messages',
        }

        @_msg : Must be MessageBlock class
        return : True/False
        """
        if not isinstance(_msg, BlockMsg):
            return False

        if self.tick():
            # every 2 seconds, flush all the queued messages
            self.flush()
        if self._counter > self._max_queue:
            ''' queued-messages are written into log files '''
            # To-Do :  - gbkim@ye24.com
            self.flush()
            # end if
        self._msg_queue.put(_msg)
        self._counter += 1

        return True
    def flush(self):
        """ flush all queued message into logger """
        while not self._msg_queue.empty():
            _tmp = self._msg_queue.get()
            if _tmp.get()['level'] == lvl.DEBUG:
                _rtmp = self.log_formater(_tmp)
                if _rtmp is not None:
                    self._debug.debug(_rtmp)
            elif _tmp.get()['level'] == lvl.ERROR:
                _rtmp = self.log_formater(_tmp)
                if _rtmp is not None:
                    self._error.debug(_rtmp)

    def close(self):
        """ """
        handlers = self._error.handlers[:]
        for handler in handlers:
            handler.close()
            self._error.removeHandler(handler)

        handlers = self._debug.handlers[:]
        for handler in handlers:
            handler.close()
            self._debug.removeHandler(handler)

    def __del__(self):
        """ in the end of this istance,
        flush all and close handlers
        """
        self.flush()
        self.close()

def main():
    tslog = ThreadSafeLogger(max_number=100)
    bmsg = BlockMsg('me','hello me')
    for i in range(1,10):
        tslog.put_message_block(bmsg)
    exit()

if __name__ == '__main__':
    main()
