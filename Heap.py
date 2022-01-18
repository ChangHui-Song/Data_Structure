# -*- coding : utf-8 -*-
from random import randrange
import heapq
import time

class min_Heap:
    def __init__(self):
        self.hp = [None]
        self.length = 1

    def insert(self, data):
        if self.hp != [None]:
            self.hp.append(data)
            i = self.length
            while i != 1:
                if self.hp[i//2] >= self.hp[i]:
                    self.hp[i//2], self.hp[i] = self.hp[i], self.hp[i//2]
                else:
                    break
                i = i//2
            self.length += 1
        else:
            self.hp.append(data)
            self.length += 1
    
    def delete(self):
        if self.length != 1:
            self.hp[1], self.hp[-1] = self.hp[-1], self.hp[1]
            idx = self.hp.pop()
            self.length -= 1
            i = 1
            
            while True:
                left = 2 * i
                right = (2 * i) + 1
                smallest = i

                if left < self.length and self.hp[i] > self.hp[left]:          
                    smallest = left

                if right < self.length and self.hp[left] > self.hp[right]:
                    smallest = right

                if smallest != i:
                    self.hp[i], self.hp[smallest] = self.hp[smallest], self.hp[i]

                i = smallest
                if i >= self.length//2:
                    break
        else:
            return "hq is empty"
            
        return idx

    def print(self):
        print(self.hp)

class max_Heap:
    def __init__(self):
        self.hp = [None]
        self.length = 1

    def insert(self, data):
        self.hp.append(data)
        if self.length == 1:
            self.length += 1
            return

        i = self.length
        while i != 1:
            if self.hp[i] >= self.hp[i//2]:
                self.hp[i], self.hp[i//2] = self.hp[i//2], self.hp[i]
                i = i//2
            else:
                break
        self.length += 1

    def delete(self):
        if self.length != 1:
            self.hp[-1], self.hp[1] = self.hp[1], self.hp[-1]
            idx = self.hp.pop()
            self.length -= 1
            i = 1

            while True:
                left = i * 2
                right = i * 2 + 1
                largest = i
                if left < self.length and self.hp[left] > self.hp[largest]:
                    largest = left
                if right < self.length and self.hp[left] < self.hp[right]:
                    largest = right
                
                if largest != i:
                    self.hp[i], self.hp[largest] = self.hp[largest], self.hp[i]
                else:
                    break
                i = largest
        else:
            return "hq is empty"

        return idx
    
    def print(self):
        print(self.hp)

if __name__ == '__main__':
    minhp = min_Heap()
    idx_li = [53, 27, 24, 10, 32, 34, 29, 46, 40, 30, 19, 47, 10, 35, 25]
    print(idx_li)
    for x in idx_li:
        minhp.insert(x)
    min_res = []
    for _ in range(len(idx_li)):
        x = minhp.delete()
        min_res.append(x)
    print(min_res)
    print()

    maxhp = max_Heap()
    for x in idx_li:
        maxhp.insert(x)
    max_res = []
    for _ in range(len(idx_li)+2):
        print(maxhp.delete())
        
    


