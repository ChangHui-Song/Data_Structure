class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.cnt = 0
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            idx = self.head
            while idx.next != None:
                idx = idx.next
            idx.next = node
        self.cnt += 1

    def size(self):
        print(self.cnt)

    def insert(self, node, idx):
        curn = self.head
        pnode = None

        if idx == 0:
            if self.head:
                next_data = self.head
                self.head = node
                self.head.next = next_data
            else:
                self.head = node
        else:
            if idx > self.cnt:
                return -1
            else:
                for _ in range(idx):
                    pnode = curn
                    curn = curn.next
                pnode.next = node
                node.next = curn
        self.cnt += 1

    def delete(self, idx):
        curn = self.head
        pnode = None
        nnode = self.head.next

        if idx == 0:
            if self.head:
                self.head = self.head.next
                del curn
            else:
                return -1
        else:
            if idx < self.cnt-1:
                for _ in range(idx):
                    pnode = curn
                    curn = curn.next
                    nnode = curn.next
                del curn
                pnode.next = nnode
            elif idx == self.cnt-1:
                for _ in range(idx):
                    pnode = curn
                    curn = curn.next
                pnode.next = None
                del curn
            else:
                return -1
        self.cnt -= 1
    
    def print_list(self):
        curn = self.head
        if curn:
            string = ''
            while curn:
                string += str(curn.data)
                if curn.next:
                    string += '->'
                curn = curn.next
            print(string)
        else:
            print('list is empty')

if __name__ == '__main__':
    sl = SinglyLinkedList()
    for i in range(1, 11):
        sl.append(Node(i))

    sl.print_list()
    sl.size()
    sl.insert(Node('a'), 6)
    sl.print_list()
    sl.size()
    sl.delete(9)
    sl.print_list()
    sl.size()
    
