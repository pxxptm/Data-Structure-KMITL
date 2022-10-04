''' กฤษฎาได้มีไอเดียสุดบรรเจิดคือการสร้างโปรแกรม Text Editor แบบ VIM ขึ้นมาใช้งานเอง โดยโปรแกรมนี้จะมีอยู่แค่ 1 Mode คือ Command Mode (inputของเรานั่นแหละ) โดยจะมีคำสั่งอยู่ 5 แบบ คือ Insert (I) , Left (L) , Right (R) , Backspace (B) และ Delete (D) (โดยความสามารถของคำสั่งต่างๆจะอธิบายด้านล่าง) แต่กฤษฎาไม่มีความสามารถทางด้านการสร้างโปรแกรมเลย กฤษฎาจึงได้มาขอร้องน้องๆที่เรียนอยู่วิศวกรรมคอมพิวเตอร์ ให้ช่วยสร้างโปรแกรม Text Editor ที่กฤษฎาต้องการให้หน่อย โดยผลลัพธ์ให้แสดงออกมาเป็น word ที่เหลืออยู่จาก Command ที่เราใส่ลงไป พร้อมกับตำแหน่งของ Cursor

***** อธิบาย Input 5 แบบ *****

1.  I <word > :   เป็นการนำ word ลงไปใส่ในตำแหน่งของ Cursor ปัจจุบัน หลังจากใส่ word เสร็จ ตำแหน่งของ Cursor จะมาอยู่ด้านหลังของ word ที่ใส่ลงไป

2.  L              :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านซ้าย 1 ตำแหน่ง หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

3.  R             :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านขวา 1 ตำแหน่ง หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร

4.  B             :   เป็นการลบ word 1 ตัวทางด้านซ้ายของ Cursor หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

5.  D             :   เป็นการลบ word 1 ตัวทางด้านขวาของ Cursor หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร '''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.linkedListSize = 0

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

    def addHead(self, item):
        if self.head is None :
            newNode = Node(item)
            self.head = newNode
            self.tail = newNode
        else :
            newNode = Node(item)
            self.head.previous = newNode
            self.head.previous.next = self.head
            self.head = newNode

    def insert(self, pos, item):
        index = 0
        newNode = Node(item)
        now = self.head
        if pos == 0 :
            self.addHead(item)
        elif pos == self.linkedListSize :
            self.append(item)
        else :
            while now != None :
                if index != pos:
                    now = now.next
                    index += 1
                else :
                    newNode.previous = now.previous
                    newNode.next = now
                    now.previous.next = newNode
                    now.previous =newNode
                    now = now.next
                    index += 1
        self.linkedListSize += 1

    def pop(self, pos) :
        index = 0
        now = self.head
        if self.linkedListSize != 0 :
            if  pos == self.linkedListSize-1 :
                now = self.tail
                now.previous.next = None
                self.tail = now.previous
            elif  pos > 0 :
                while now != None :
                    if pos == index:
                        now.previous.next = now.next
                        now.next.previous = now.previous
                    index +=1
                    now = now.next
            elif pos == 0 and self.linkedListSize == 1:
                self.head = None
                self.tail = None
            elif pos == 0 :
                now.next.previous = None
                self.head = now.next
        self.linkedListSize -= 1


    def index(self, pos):
        now = self.head
        index = 0
        while now != None:
            if index == pos :
                return now.value
            else :
                index += 1
            now = now.next


input = input("Enter Input : ").split(",")

ll = LinkedList()
cursorPos = 0
i = 1

for element in input :
    if element == "L" :
        if cursorPos > 0 :
            cursorPos -= 1
    elif element == "R" :
        if cursorPos < ll.linkedListSize :
            cursorPos += 1
    elif element == "B" :
        if cursorPos-1 >= 0 :
            cursorPos -= 1
            ll.pop(cursorPos)
    elif element == "D" :
        if cursorPos <= ll.linkedListSize-1 :
            ll.pop(cursorPos)
    else :
        temp = element.split()
        ll.insert(cursorPos,temp[1])
        cursorPos += 1

ll.insert(cursorPos,"|")

print(ll)