class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
def printLevelOrder(root):
    res = []
    if root is None:
        return res
    queue = []
    queue.append(root)
    while len(queue)>0:
        res.append(queue[0].data)
        # print(que[0].data)
        node = queue.pop(0)
        
        if node.left!= None:
            queue.append(node.left)
        if node.right!= None:
            queue.append(node.right)
            
    print (res)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)

printLevelOrder(root)