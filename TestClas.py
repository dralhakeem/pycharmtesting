#!/usr/bin/python
# -*- encoding: utf-8 -*-

__author__ = 'Alhakeem'


class Stack(object):
    """testing the declaration of a class."""

    count = 0

    def __init__(self) :  # constructor
        self.items = []  # Instance Variable accessed by instance name
        Stack.count += 1  # Class variable accessed by class name Stack

    def push(self,x):
        self.items.append(x)

    def pop(self):
        x=self.items[-1]
        del(self.items[-1])
        return x

    def __del__(self):  # Destructor
        if Stack:
            Stack.count -= 1

    def __ichBinGeheim(self):
        print ('testing private method')

    def _ichBinGeschutzt(self):
        print ('testing protected method')


class LimitedStack(Stack):
    """a limited stack"""
    def __init__(self, limit):
        self.limit = limit
        Stack.__init__(self) # base class constructor

    def push(self,x):
        assert len(self.items) < self.limit
        Stack.push(self,x) # calling the supper method

    def __str__(self):
        s =  "I am a stack that have the length of {} and the following elements {}".format(len(self.items), self.items)
        return s

if __name__ == '__main__':  # executed if the script is executed directly
    s = Stack()
    s1 = Stack()
    s2 = LimitedStack(20)
    s.push(34)
    s2.push(5)
    print(s.pop())
    # s.__ichBinGeheim()
    s._ichBinGeschutzt()
    print(s)  # returns type and address
    print(s2)  # returns the newly defined __str__
    del(s)
    print (Stack.count)
