#!/usr/bin/python
# -*- encoding: utf-8 -*-

__author__ = 'Alhakeem'


class Stack(object):
    ''' testing the declaration of a class.
    '''
    def __init__(self): #constructor
        self.items = [] #Instance Variable

    def push(self,x):
        self.items.append(x)

    def pop(self):
        x=self.items[-1]
        del(self.items[-1])
        return x+1



if __name__ == '__main__': # executed if the script is executed directly
    s = Stack()
    s.push(34)
    print(s.pop())

