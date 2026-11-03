from heap import ArrayHeap

class PriorityQueue:

    def __init__(self):
        
        self.heap = ArrayHeap()

    def push(self, data):

        self.heap.add(data)

    def pop(self):

        return self.heap.pop()

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
