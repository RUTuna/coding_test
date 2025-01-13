import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, x, idx):
        self.x = x
        self.idx = idx
        self.left = None
        self.right = None
        
def insert(parent, child):
    if child.x < parent.x:
        if not parent.left:
            parent.left = child
        else:
            insert(parent.left, child)
    else:
        if not parent.right:
            parent.right = child
        else:
            insert(parent.right, child)
            
def solution(nodeinfo):
    nodes = [(x, y, i + 1) for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda x: (-x[1], x[0]))
    root = Node(nodes[0][0], nodes[0][2])
    
    for x, _, i in nodes[1:]:
        insert(root, Node(x, i))
    
    preOrder, postOrder = [], []
    
    def DFS(now):
        preOrder.append(now.idx)
        if now.left:
            DFS(now.left)
        if now.right:
            DFS(now.right)
        postOrder.append(now.idx)
        
        
    DFS(root)
        
    return [preOrder, postOrder]