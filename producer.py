#-------------------------------------------------------------------------------
# Name:        LinkProducer
# Purpose:     Producer generates Target Links
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
import threading
from safe_logger import ThreadSafeLogger as tsl
from simple_request_wrapper import LinkRequest as linkReq
from base_object import baseObject
import numpy as np

class LinkProducer(baseObject):
    def __init__(self, _tsl, name):
        baseObject.__init__(self,_tsl)
        # check whether threadsafelogger is ot not
        if not isinstance(_tsl, tsl):
            raise TypeError("_tsl should be ThreadSafeLogger")

        self._lin_req = linkReq()
        self._nm = name
        self._pool = np.random.randint(low=0, high=90000, size=5000, dtype='I').tolist()


    def run(self):
        """ access to the link generate url
        fetch redirect url
        안정적으로 쓰레드를 관리하기 위한 방법이 필요
        """
        ret = self._lin_req.transfer_request(self._pool.pop())
        print(self._pool.pop())
        self.report(self._nm, "get {0}".format(ret))
        pass

def main():
    _tsl = tsl(100) # ThreadSafeLogger can handle 100 threads
    lp = LinkProducer(_tsl,"pathfinder")
    lp.start()

    lp.join()
    pass

if __name__ == '__main__':
    main()
