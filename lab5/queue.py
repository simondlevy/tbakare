from linkedlist import LinkedList
from linkedlist import Node

class Queue:

    def __init__(self):
        
        self.list = LinkedList()

    def push(self, data):

        node = Node(data)
        
        if self.list.head is None:
            self.list.head = node

        else:
            self.list.tail.next = node

            node.prev = self.list.tail
            
        self.list.tail = node

    def pop(self):

        if self.list.head is None:
            return None

        value = self.list.head.data

        self.list.head = self.list.head.next

        return value

if __name__ == '__main__':

    s = Queue()

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
