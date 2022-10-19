from collections import deque 

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def reverseLevelOrder(root):
    # code here
    q,ans = deque(), deque()
    q.append(root)
    
    while q:
        node = q.popleft()
        if node is None:
            continue
        ans.appendleft(node.data)
        
        if node.right:
            q.append(node.right)
            
        if node.left:
            q.append(node.left)
            
    print (ans)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)

reverseLevelOrder(root)