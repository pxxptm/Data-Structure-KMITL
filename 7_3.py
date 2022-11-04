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
    
def countLess(root,val):
    if root:
        countLess(root.left,val)
        if int(root.data) <= int(val):
            ans.append(root.data)
        countLess(root.right,val)
        

T = BST()
ans = []
inp,aim = input('Enter Input : ').split("/")
inp = [int(i) for i in inp.split()]
for i in inp:
    root = T.insert(i)
    
T.printTree(root)
print("--------------------------------------------------")
countLess(T.root,aim)
print(len(ans))  