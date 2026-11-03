
from priorityqueue import PriorityQueue as PQ1
from priorityqueue2 import PriorityQueue as PQ2
from tqdm import tqdm

def test(q):

    N = 10_000_000

    for item in tqdm(range(N)):
        q.push(item)

if __name__ == '__main__':

    print("Testing Linked List Priority Queue")
    test1 = PQ1()
    test(test1)
    
    print("\nTesting Array Heap Priority Queue")
    test2 = PQ2()
    test(test2)
