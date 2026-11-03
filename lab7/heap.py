
class ArrayHeap:

    def __init__(self):

        self.heap = list()
        self.size = 0

    def __contains__(self, item):

        if item in self.heap:
            return True

        return False

    def __str__(self):

        return str(self.heap)

    def add(self, item):
        self.size += 1
        self.heap.append(item)
        curPos = len(self.heap) - 1
        while curPos > 0:
            parent = (curPos - 1) // 2
            parentItem = self.heap[parent]
            if parentItem <= item:
                break
            else:
                self.heap[curPos] = self.heap[parent]
                self.heap[parent] = item
                curPos = parent

    def pop(self):
        self.size -= 1
        try:
            topItem = self.heap[0]
        except IndexError:
            return None
        bottomItem = self.heap.pop(len(self.heap) - 1)
        if len(self.heap) == 0:
            return bottomItem
               
        self.heap[0] = bottomItem
        lastIndex = len(self.heap) - 1
        curPos = 0
        while True:
            leftChild = 2 * curPos + 1 
            rightChild = 2 * curPos + 2
            if leftChild > lastIndex:
                break
            if rightChild > lastIndex:
                maxChild = leftChild;
            else:
                leftItem  = self.heap[leftChild]
                rightItem = self.heap[rightChild]
                if leftItem < rightItem:
                    maxChild = leftChild
                else:
                    maxChild = rightChild
            maxItem = self.heap[maxChild]
            if bottomItem <= maxItem:
                break
            else:
                self.heap[curPos] = self.heap[maxChild]
                self.heap[maxChild] = bottomItem
                curPos = maxChild
        return topItem



if __name__ == '__main__':

    print("Added in-order heap")
    heap = ArrayHeap()

    heap.add(2)
    heap.add(3)
    heap.add(4)
    heap.add(5)
    heap.add(6)
    heap.add(7)
    heap.add(8)

    print(heap)
    print("Heap Contains 5, Expect True:", 5 in heap)
    print("Heap Contains 20, Expect False:", 20 in heap)
    print("Popped item: ", heap.pop())
    print("Updated list: ", heap)


    print()
    print("Randomly added heap")
    unb = ArrayHeap()

    unb.add(25)
    unb.add(6)
    unb.add(40)
    unb.add(13)
    unb.add(7)
    unb.add(2)
    unb.add(8)
    
    print(unb)
    print("Heap Contains 25, Expect True:", 25 in unb)
    print("Heap Contains 100, Expect False:", 100 in unb)
    print("Popped item: ", unb.pop())
    print("Updated list: ", unb)
