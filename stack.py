class Node:
    def __init__ (self, data):
        self.data = data
        self.prev = None

class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, data):
        new = Node(data)
        new.prev = self.top
        self.top = new
    
    def pop(self):
        if self.top is None:
            return None
        
        data = self.top.data
        self.top = self.top.prev
        return data # garbage collector가 자동으로 메모리 관리를 해주기에 별도 관리 필요 X
    
    def peek(self):
        if self.top is None:
            return None
        
        return self.top.data
    
    def isEmpty(self):
        return self.top is None
    
    