class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def left_append(self, data):
        node = Node(data)
        if self.head:
            tmp = self.head
            self.head = node
            self.head.next = tmp
            tmp.prev = self.head
        else:
            self.head = node
            self.tail = self.head
        self.size += 1

    def right_append(self, data):
        node = Node(data)
        if self.tail:
            tmp = self.tail
            self.tail = node
            node.prev = tmp
            tmp.next = self.tail
        else:
            self.head = node
            self.tail = self.head
        self.size += 1

    def left_pop(self):
        if self.head == None:
            return -1
        tmp = self.head
        self.head = self.head.next
        self.size -=1
        return tmp.data

    def right_pop(self):
        if self.tail == None:
            return -1
        tmp = self.tail
        self.tail = self.tail.prev
        self.size -=1
        return tmp.data

    def simple_print(self):
        tmp = self.head
        for _ in range(self.size-1):
            print(tmp.data, end=' <-> ')
            tmp = tmp.next
        print(tmp.data)

    def list_size(self):
        return self.size

if __name__ == '__main__':
    dq = Deque()
    for i in range(5, -1, -1):
        dq.left_append(i)
    for i in range(6, 11):
        dq.right_append(i)
    print(dq.list_size())
    dq.simple_print()
    dq.left_pop()
    dq.right_pop()
    print(dq.list_size())
    dq.simple_print()
    