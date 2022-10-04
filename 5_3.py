''' ให้น้องรับ Linked List มา 2 ตัว จากนั้นนำ 2 Linked List มาต่อกัน โดย L2 จะมาต่อ L1 แบบกลับหลัง '''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head is None :
          newNode = Node(item)
          self.head = newNode
          self.tail = newNode
        else :
            now = self.tail
            newNode = Node(item)
            now.next = newNode
            newNode.previous = self.tail
            self.tail = newNode

    def size(self):
        size = 0
        now =self.head
        while now != None:
            size += 1
            now = now.next
        return size

def mergeList (input1,input2) :
    L1 = LinkedList()
    L2 = LinkedList()

    for element in input1 :
        L1.append(element)

    for element in input2 :
        L2.append(element)

    print("L1    :",L1)
    print("L2    :",L2)

    it = L2.tail

    while it != L2.head :
        L1.append(it.value)
        it = it.previous
        
    L1.append(it.value)

    print("Merge :",L1)


input1,input2 = input("Enter Input (L1,L2) : ").split()

if "->" in input1 :
    input1 = input1.split("->")

if "->" in input2 :
    input2 = input2.split("->")

mergeList(input1,input2)