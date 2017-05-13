#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      YES24
#
# Created:     19-04-2017
# Copyright:   (c) YES24 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

with open('ArtContents.html','r', encoding='utf8') as r:
    x = r.read()

from bs4 import BeautifulSoup as bs
root = bs(x,'lxml')

for u in root.recursiveChildGenerator():
    try:
        print(u.attrs)
    except AttributeError:
        # print(u)
        # has a child
        pass
    pass

