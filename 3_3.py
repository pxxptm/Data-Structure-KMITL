'''
    ให้รับ Input เป็น  Infix  และแสดงผลลัพธ์ออกมาเป็น  Postfix   โดยจะมี Operator  5  แบบ  ได้แก่  +   -   *   /   ^


    class Stack:

        def __init__(self):

        def push(self, value):

        def pop(self):

        def size(self):

        def isEmpty(self):

    inp = input('Enter Infix : ')

    S = Stack()

    print('Postfix : ', end='')

    ### Enter Your Code Here ###

    while not S.isEmpty():
        print(S.pop(), end='')

    print()
'''

OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3} 

class Stack:

    items = []

    def __init__ (self , list = None) :
        if list == None :
            self.items = []
        else :
            self.items = list

    def push(self,value) :  
        self.items.append(value)

    def pop(self) :  
        return self.items.pop()

    def peek(self) :  
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self) :
        return len(self.items)     

inp = input('Enter Infix : ')

S = Stack()

output =""
print('Postfix : ', end='')

for ch in inp :

        if ch not in OPERATORS : 
            output += ch

        elif ch=='(': 
            S.push('(')

        elif ch==')':
            while (not S.isEmpty()) and S.peek()!= '(':
                output+=S.pop()
            S.pop()

        else:
            while (not S.isEmpty()) and S.peek()!='(' and PRIORITY[ch]<=PRIORITY[S.peek()]:
                output+=S.pop()
            S.push(ch)

while not S.isEmpty() :
    output += S.pop()

print(output)