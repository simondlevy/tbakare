from linkedlist import LinkedList
from linkedlist import Node

class PriorityQueue:

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

    def push(self, item):
        node = Node(item)
        position = None
        
        if self.list.head is None:
            self.list.head = node
            self.list.tail = node
            position = 0
            
        elif item >= self.list.tail.data:
            self.list.tail.next = node
            node.prev = self.list.tail
            self.list.tail = node
            position = "last"
            
        elif item < self.list.head.data:
            node.next = self.list.head
            self.list.head.prev = node
            self.list.head = node
            position = 0

        else:
            position = 1
            first = self.list.head
            second = self.list.head.next
            while item >= first.data and item >= second.data:
                first = first.next
                second = second.next
                position += 1
            first.next = node
            second.prev = node
            node.prev = first
            node.next = second

        return position

    def pop(self):

        if self.list.head is None:
            return None

        value = self.list.head.data

        self.list.head = self.list.head.next

        return value

if __name__ == '__main__':

    s = PriorityQueue()
    a = PriorityQueue()

    s.push(2)
    s.push(3)
    s.push(5)
    s.push(7)
    s.push(11)
    s.push(1)
    s.push(4)
    s.push(5)
    s.push(6)

    a.push('c')
    a.push('d')
    a.push('a')
    a.push('f')
    a.push('e')
    a.push('b')

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
