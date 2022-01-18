# -*- coding: utf-8 -*-
import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.li = []

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        curn = self.root

        while True:
            if curn == None:
                self.root = Node(data)
                break
            else:
                if curn.data > data:
                    if curn.left:
                        curn = curn.left
                    else:
                        curn.left = Node(data)
                        break
                else:
                    if curn.right:
                        curn = curn.right
                    else:
                        curn.right = Node(data)
                        break
    
    def find(self, val):
        cur = self.root
        res = False
        while True:
            if cur == None:
                break
            elif val > cur.data:
                cur = cur.right
            elif val < cur.data:
                cur = cur.left
            else:
                res = True
                break
        return res
        
    def delete(self, val):
        curPnode = None
        curnode = self.root

        if self.find(val) == False:
            return False

        while True:
            if curnode.data == val:
                break
            else:
                curPnode = curnode
                if curnode.data < val:
                    curnode = curnode.right
                else:
                    curnode = curnode.left

        if curnode.left == None and curnode.right == None:
            if curPnode.left == curnode:
                curPnode.left = None
                del curnode
            else:
                curPnode.right = None
                del curnode
        elif curnode.left != None and curnode.right != None:
            subPnode = None
            subnode = curnode
            while subnode.right != None:
                subnode = subnode.right
            while subnode.left != None:
                subPnode = subnode
                subnode = subnode.left
            if subnode.right != None:
                subPnode.left = subnode.right
            curPnode.right = subnode
            subnode.left, subnode.right = curnode.left, curnode.right
            del curnode

        else:
            if curnode.left != None:
                if curPnode.left == curnode:
                    curPnode.left = curnode.left
                else:
                    curPnode.right = curnode.left
                del curnode
            else:
                if curPnode.left == curnode:
                    curPnode.left = curnode.right
                else:
                    curPnode.right = curnode.right
                del curnode

    def preorder_traversal(self):
        def _preorder_traversal(val):
            if self.root != None:
                print(val.data, end=' ')
                if val.left != None:
                    _preorder_traversal(val.left)
                if val.right != None:
                    _preorder_traversal(val.right)
        _preorder_traversal(self.root)
        print()

    def inorder_traversal(self):
        def _inorder_traversal(val):
            if self.root != None:
                if val.left != None:
                    _inorder_traversal(val.left)
                print(val.data, end=' ')
                if val.right != None:
                    _inorder_traversal(val.right)
        _inorder_traversal(self.root)
        print()
    
    def postorder_traversal(self):
        def _postorder_traversal(val):
            if self.root != None:
                if val.left != None:
                    _postorder_traversal(val.left)
                if val.right != None:
                    _postorder_traversal(val.right)
                print(val.data, end=' ')
        _postorder_traversal(self.root)
        print()

    #used Queue.py
    def breadth_first_traversal(self):
        que = Queue.Queue()
        def _breadth_first_traversal(val):
            que.enqueue(val) 
            while que:
                val = que.dequeue()
                if val != None:
                    print(val.data.data, end=" ")
                    if val.data.left != None:
                        que.enqueue(val.data.left)
                    if val.data.right != None:
                        que.enqueue(val.data.right)
                else:
                    print()
                    break
        _breadth_first_traversal(self.root)

if __name__ == '__main__':
    tr = BinarySearchTree()
    li = [40, 6, 34, 45, 15, 55, 48, 13, 16, 49, 47, 14, 44, 47.5]

    print(li)
    for x in li:
        tr.insert(x)
    # tr.preorder_traversal()
    # tr.inorder_traversal()
    # tr.postorder_traversal()
    tr.breadth_first_traversal()
    # print(tr.find(55))
    tr.delete(55)
    tr.breadth_first_traversal()