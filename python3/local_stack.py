#!/usr/bin/env python3

class stack:
    def __init__(self):
        self.s = []

    def push(self, v):
        self.s.append(v)

    def pop(self):
        return self.s.pop()

    def top(self):
        return self.s[-1]

    def empty(self):
        return self.s == []
        
    def clear(self):
        self.s = []
    
class forth_stack(stack):
    def swap(self):
        r = self.pop() #  l op r
        l = self.pop()
        self.push(r)
        self.push(l)   #  r op l

    def dup(self):
        self.push(self.top())

    def inc(self):
        self.push(self.pop() + 1)

    def add(self):
        self.push(self.pop() + self.pop())

    def sub(self):
        self.swap() 
        self.push(self.pop() - self.pop())

    def mul(self):
        self.push(self.pop() * self.pop())

    def div(self):
        self.swap() 
        self.push(self.pop() // self.pop())

def test(s):
    s.push(1)
    assert s.pop() == 1
    assert s.empty()
    
    s.push(1)
    assert s.top() == 1
    assert s.pop() == 1
    assert s.empty()
    
    s.push(1)
    s.dup()
    assert s.pop() == 1
    assert s.pop() == 1
    assert s.empty()

    s.push(1)
    s.push(2)
    assert not s.empty()
    s.clear()
    assert s.empty()
    
    s.clear()
    s.push(0)
    s.inc()
    s.inc()
    assert s.pop() == 2
    assert s.empty()
    
    s.clear()
    s.push(2)
    s.push(3)
    s.add()
    assert s.pop() == 5
    assert s.empty()
    
    s.clear()
    s.push(2)
    s.push(3)
    s.sub()
    assert s.pop() == -1
    assert s.empty()

    s.clear()
    s.push(2)
    s.push(3)
    s.mul()
    assert s.pop() == 6
    assert s.empty()

    s.clear()
    s.push(2)
    s.push(3)
    s.div()
    assert s.pop() == 0
    assert s.empty()

    s.clear()
    s.push(3)
    s.push(2)
    s.div()
    assert s.pop() == 1
    assert s.empty()
    

if __name__ == '__main__':
    s = forth_stack()
    test(s)
