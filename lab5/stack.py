from linkedlist import LinkedList
from linkedlist import Node

class Stack:

    def __init__(self):
        
        self.list = LinkedList()

    def __iter__(self):

        node = self.list.head

        while node is not None:
            yield node.data
            node = node.next

    def push(self, data):

        node = Node(data)
        
        if self.list.head is None:
            self.list.head = node

        else:
            self.list.tail.next = node

            node.prev = self.list.tail
            
        self.list.tail = node

    def pop(self):

        if self.list.tail is None:
            return None

        value = self.list.tail.data

        self.list.tail = self.list.tail.prev

        if self.list.tail is not None:
            self.list.tail.next = None
        else:
            self.list.head = None

        return value

    def isEmpty(self):

        if self.list.head is None:
            return True

    def __len__(self):
        n = 0
        node = self.list.head

        while node is not None:
            n += 1
            node = node.next

        return n

if __name__ == '__main__':

    s = Stack()

    s.push(2)
    s.push(3)
    s.push(5)
    s.push(7)
    s.push(11)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
