#-------------------------------------------------------------------------------
# Name:        MainThruster
# Purpose:     Get Threads Started and Manage/Monitor Objects
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

from safe_logger import ThreadSafeLogger as tsl
from messages import MessageBlock as msgb
from threading import Event

class MainThruster:
    """ MainThruster """
    def __init__(self):
        """ Manages Object """
        self._tsl = tsl(100) # ThreadSafeLogger can handle 100 threads
        #self._lpro =

        pass
    def run(self):
        while True:
            self._tsl.put_message_block(msgb('MainThruster', 'This Message isn\'t valid '))


    def test(self):
        """ test for docstrings """
        m= msgb('MainThruster', 'This Message isn\'t valid ')
        self._tsl.put_message_block(m)

def main():
    thruster = MainThruster()
    thruster.run()

if __name__ == '__main__':
    main()
