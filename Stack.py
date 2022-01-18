class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def push(self, data):
        if self.head:
            tmp = self.head
            self.head = Node(data)
            self.head.next = tmp
        else:
            self.head = Node(data)
        self.size += 1

    def pop(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data
        else:
            return -1
        
    def peak(self):
        if self.head:
            return self.head.data
        else:
            return -1

    def size(self):
        return self.size

    def print_st(self):
        curn = self.head
        for _ in range(self.size):
            print(curn.data, end = '')
            curn = curn.next
        print()

if __name__ == '__main__':
    st = Stack()
    
    for i in range(10):
        st.push(i)
    st.print_st()
    print(st.peak())
    st.print_st()
    print(st.pop())
    st.print_st()