# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:59:51 2018

@author: jorda

"""

class Node:
    def __init__(self,data,parent,path,heuristic):
        self.parent = parent
        self.value = data
        self.g = path
        self.h = heuristic
        self.f = self.g + self.h
        
    def gethValue(self):
        value = self.h
        return value
        
alist = [5,4,8,3,5,8,9,12,1]
alist.sort()
print("int sort: " + str(alist))

alist = [5.65,5.95,12,12.5,13.5,.95,5]
alist.sort()
print("double sort: " + str(alist))

one = Node([1,1],0,0,25)
two = Node([2,2],0,0,15)
three = Node([2,2],0,0,5)

blist = [one,two,three]
blist.sort(key=lambda x: x.h, reverse=False)

heap = []
#for x in range(len(blist)):
#    value=blist[x].gethValue()
#    heap.append(value)
    
heap.sort()
print("h value sort: " + str(heap))
print("node sort: " +str(blist))
for x in range(len(blist)):
    print(blist[x].h)



