from random import choice

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class Player:
    def __init__(self, text=None):
        self.text = text
        self.next = None

    def shuffle(self, text):
        listtext =

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            # stack
            # old_link = self.head
            # self.head = node
            # self.head.next = old_link
            # queue
            head = self.head
            while head.next:
                head = head.next
            head.next = node

    def get_all(self):
        head = self.head
        nodes = []
        while head:
            nodes.append(head.value)
            head = head.next
        return nodes

mylist = LinkedList()
mylist.add()
print(mylist.get_all())
