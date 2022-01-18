class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0

    def enqueue(self, data):
        if self.head:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        else:
            self.head = Node(data)
            self.tail = self.head
        self.cnt += 1
        
    def dequeue(self):
        if self.head:
            curn = self.head
            self.head = self.head.next
            self.cnt -= 1
            return curn
        # else:
        #     return -1

    def simple_print(self):
        curn = self.head
        for _ in range(self.cnt):
            print(curn.data, end=' ')
            curn = curn.next
        print()

    def size(self):
        return self.cnt

if __name__ == '__main__':
    que = Queue()

    for i in range(11):
        que.enqueue(i)
    print(que.size())
    que.simple_print()
    for _ in range(3):
        que.dequeue()
    print(que.size())
    que.simple_print()
    
    
