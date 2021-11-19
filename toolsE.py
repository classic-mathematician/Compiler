class Node:


    def __init__(self):
        self.DIM = None
        self.R = None
        self.limS = None
        self.OS = None
        self.next = None
        self.m = None


class LinkedList:


    def __init__(self):
        self.head = None


    def printList(self):
        temp = self.head
        while (temp):
            print (temp.DIM)
            temp = temp.next


    def tail(self):
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        return temp
