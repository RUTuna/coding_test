class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    
    def enqueue(self, data):
        new = Node(data)
        
        if self.rear is None:
            self.front = new
        else:
            self.rear.next = new
            
        self.rear = new
       
        
    def dequeue(self):
        if self.front is None:
            return None
        
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else :
            self.front = self.front.next
            
        return data
    
    
    def peek(self):
        if self.front is None:
            return None
        
        return self.front.data
        
    
    def isEmpty(self):
        return self.front is None
        