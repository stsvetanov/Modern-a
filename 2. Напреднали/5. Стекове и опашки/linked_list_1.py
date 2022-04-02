class Node:
    def __init__(self, data=None):
        self.data = data
        self.nxt = None
        
class LinkedList:
    def __init__(self):
        self.front = None
    def append(self,value):
        if self.front == None:
        # добавяне към празен списък
            self.front = Node(value)
        else:# добавяне в края на не празен списък
            current = self.front
            while current.next != None:
                current = current.next
            current.next = Node(value)
    def get(self, index):
       current = self.front
       for i in range(index):
          current = current.next
          return current.data
    def insert(self, index, value):
        front = self.front
        if index == 0:
           # добавяне в началото
           self.front = Node(value, front)
        else:
            #добавяне към не празен списък в дадена позиция
            
            current = front
            for i in range(index):
                current = current.next
                current.next = Node(value, current.next)

    def remove(self, index):
        if index == 0:
            # граничен случай: премахваме първи елемент
            self.front = self.front.next
        else:# общ случай
            current = self.front
            for i in range(index):
                current = current.next
            current.next = current.next.next
    def addSorted(self, value):
        if (self.front==None or value<=self.front.data): # вмъкваме в началото
            self.front = Node(value, self.front)
        else:# вмъкваме по средата
            current = self.front
            while (current.next != None) and (current.next.data < value):
                current = current.next
#Code testing
import time
k=1000000
ll=[]
t1=time.time()
for x in range(k):ll.append(x)
t2=time.time()
lst=LinkedList()
t3=time.time()

lst.append(0)
for i in range(1,k):
    lst.front.nxt=Node(i)
t4=time.time()

import collections
lst = collections.deque()
for x in range(k):lst.append(x)
t5=time.time()
k1=t2-t1
k2=t4-t3
k3=t5-t4

if k1<=k2<=k3 or k1<=k3<=k2: print("list is faster"+str(k1))
else: pass
if k2<=k1<=k3 or k2<=k3<=k1: print("linkedlist is faster"+str(k2))
else: pass
if k3<=k1<=k2 or k3<=k2<=k1: print("collection linked list is faster "+str(k3))
else: pass


