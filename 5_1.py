''' สร้าง method insert ในคลาส LinkedList เพื่อแทรกข้อมูลลงใน index ที่กำหนดของ linked list และ return ผลลัพธ์ตามตัวอย่าง 

โดยคลาส LinkedList จะประกอบไปด้วย

1. def __init__(self): สำหรับสร้าง linked list

2. def __str__(self): return string แสดง ค่าใน linked list

3. def isEmpty(self): return list นั้นว่างหรือไม่

4. def append(self, data): เพิ่ม data ต่อท้าย linked list

5. def insert(self, index, data): insert data ใน index ที่กำหนด

โดยการแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 

คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Header Node ดูนะครับ

*******ให้ใช้ class Node ในการทำ Linked List ห้ามใช้ list*********

class Node:
    def __init__(self, data):
        self.data = data
     

ข้อมูลอินพุท จะคั่นด้วยเครื่องหมาย คอมม่า

ตัวแรก จะเป็น ลิสต์ตั้งต้น คั่นด้วยช่องว่าง (space)

ตัวต่อไปจะอยู่ในรูปแบบ index:data '''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.linkedListSize = 0

    def __str__(self):
        if self.isEmpty() :
            return "List is empty"
        s = "link list : "
        now = self.head
        while now.next is not None :
            s += str(now.data) + "->"
            now = now.next
        s += now.data
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        newNode = Node(item)
        if self.head is None :
            self.head = newNode
        else :
            now = self.head
            while now.next :
                now = now.next
            now.next = newNode
        self.linkedListSize += 1

    def insert(self, pos, item):
        newNode = Node(item)
        now = self.head

        if pos == 0 :
            newNode.next = self.head
            self.head = newNode
            self.linkedListSize += 1
        else :
            for index in range(pos-1) :
                now = now.next
            
            if now is not None :
                newNode.next = now.next
                now.next = newNode
                self.linkedListSize += 1

input = input("Enter Input : ").split(",")

ll = LinkedList()
data = input[0].split()


if ":" in input[0] :
    pass
else :
    for i in data :
        ll.append(i)

for i in range (1,len(input)) :
    print(ll)
    temp = input[i].split(":")
    pos = int(temp[0])
    if pos < 0 or pos > ll.linkedListSize :
        print("Data cannot be added")
    elif pos == ll.linkedListSize :
        print("index =",pos,"and data =",int(temp[1]))
        ll.append(temp[1])
    else :
        print("index =",pos,"and data =",int(temp[1]))
        ll.insert(pos,temp[1])

print(ll)