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

import pickle

def make_pickle():
    tag_list = []
    atr_list = []
    with open('tag.list','r') as r:
        for x in r.readlines():
            x = x.strip().lstrip().rstrip()
            tag_list.append(x)

    with open('attr.list','r') as r:
        for x in r.readlines():
            x = x.strip().lstrip().rstrip()
            atr_list.append(x)


    with open('tag.pickle', 'wb') as w:
        pickle.dump(tag_list,w)

    with open('attr.pickle', 'wb') as w:
        pickle.dump(atr_list,w)

    pass
def load_pickle():
    with open('tag.pickle','rb') as r:
        t_lst = pickle.load(r)

    print (t_lst)

    with open('attr.pickle','rb') as r:
        a_lst = pickle.load(r)
    print(a_lst)

# Done
#make_pickle()
#load_pickle()
