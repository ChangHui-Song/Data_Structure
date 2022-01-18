class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        if self.head:
            tmp = self.tail
            self.tail = Node(data)
            tmp.next = self.tail
            self.tail.prev = tmp
        else:
            self.head = Node(data)
            self.tail = self.head
        self.size += 1
    
    def append(self, data):
        if self.tail:
            tmp = self.tail
            self.tail = Node(data)
            self.tail.prev = tmp
            tmp.next = self.tail
        else:
            self.head = Node(data)
            self.tail = self.head
        self.size += 1

    def insert(self, data, idx):
        if idx > self.size-1:
            return -1

        if idx == 0:
            tmp = self.head
            self.head = Node(data)
            self.head.next = tmp
            tmp.prev = self.head
        elif idx == self.size-1:
            tmp = self.tail
            self.tail = Node(data)
            self.tail.prev = tmp
            tmp.next = self.tail
        else:
            if idx <= self.size//2:
                curn = self.head
                for _ in range(idx-1):
                    curn = curn.next
                tmp, tmp2 = curn, curn.next
                node = Node(data)
                tmp.next = node
                tmp2.prev = node
                node.prev = tmp
                node.next = tmp2
            else:
                curn = self.tail
                for _ in range(self.size-1, idx-1, -1):
                    curn = curn.prev
                node = Node(data)
                tmp = curn.next
                curn.next = node
                node.prev = curn
                tmp.prev = node
                node.next = tmp
        self.size += 1

    def delete(self, idx):
        if idx > self.size-1:
            return -1
        
        if idx == 0:
            tmp = self.head
            self.head = tmp.next
            del tmp
        elif idx == self.size-1:
            tmp = self.tail
            self.tail = tmp.prev
            del tmp
        else:
            if idx <= (self.size-1)//2:
                tmp = self.head
                for _ in range(idx):
                    tmp = tmp.next
                prev, next = tmp.prev, tmp.next
                prev.next = next
                next.prev = prev
                del tmp
            else:
                tmp = self.tail
                for _ in range(self.size-1, idx, -1):
                    tmp = tmp.prev
                prev, next = tmp.prev, tmp.next
                prev.next = next
                next.prev = prev
                del tmp
        self.size -= 1
        
    def simple_print(self):
        curn = self.head
        string = ''
        for _ in range(self.size-1):
            string += str(curn.data)
            string += ' <-> '
            curn = curn.next
        string += str(curn.data)
        print(string)

    def list_size(self):
        return self.size

if __name__ == '__main__':
    dl = DoublyLinkedList()

    for i in range(11):
        dl.add(i)
    dl.append(11)
    print(dl.list_size())
    dl.simple_print()
    dl.insert('a', 9)
    print(dl.list_size())
    dl.simple_print()
    dl.delete(9)
    print(dl.list_size())
    dl.simple_print()
    
    
        