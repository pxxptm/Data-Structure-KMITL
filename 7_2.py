class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None :
            self.root = Node(data)
        else :
            now = self.root
            while True :
                if data < now.data :
                    if now.left == None :
                        now.left = Node(data)
                        break
                    else :
                        now = now.left
                else :
                    if now.right == None :
                        now.right = Node(data)
                        break
                    else :
                        now = now.right
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
def printInorder(root,val):
    if root:
        printInorder(root.left,val)
        if int(root.data) < int(val):
            print(root.data,end =" ")
        printInorder(root.right,val)

def minValue(node):
    now = node
    while(now.left is not None):
        now = now.left
    return now.data
        

T = BST()
inp,aim = input('Enter Input : ').split("|")
inp = [int(i) for i in inp.split()]
for i in inp:
    root = T.insert(i)
    
T.printTree(root)
print("--------------------------------------------------")
print("Below",aim,":",end=" ")
if minValue(T.root) < int(aim) : 
    printInorder(T.root,aim)  
else :
    print("Not have")