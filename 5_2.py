'''ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้
1. __init__     สร้าง Head ขึ้นมาเพื่อบอกว่าจุดเริ่มต้นของ Linked List คือตรงไหน
2. __str__     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่หัวไปจนท้ายมีตัวอะไรบ้าง
3. reverse     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่ท้ายไปจนหัวมีตัวอะไรบ้าง
4. isEmpty    เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
5. append     add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
6. addHead  add Item เข้า Linked List จากด้านหน้า ไม่คืนค่า
7. search      ค้นหา Item ที่ต้องการใน Linked List คืนค่าเป็น Found / Not Found
8. index        ค้นหา Item ที่ต้องการใน Linked List ว่าอยู่ที่ Index ไหน คืนค่าเป็น Index (0,1,2,3,4,.....) ถ้าหากไม่มีคืนค่าเป็น -1
9. size           คืนค่าเป็นขนาดของ Linked List
10. pop         นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range
11. insert       เป็นการนำ Item ไปแทรกใน Linked List ตามตำแหน่ง pos ไม่มีการคืนค่า

ถ้าน้องยังไม่ค่อยเข้าใจการทำงานของ insert ให้น้องลองกับ List บน Python ได้  เช่น
1.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(0,"T") จะได้ผลลัพธ์คือ [ "T", 0 , 1 , 2 , 3 ]
2.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(999,"T") จะได้ผลลัพธ์คือ [ 0 , 1 , 2 , 3 , "T" ]
3.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(-2,"T") จะได้ผลลัพธ์คือ [ 0 , 1 , "T" , 2 , 3 ]  
4.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(-10,"T") จะได้ผลลัพธ์คือ [ "T", 0 , 1 , 2 , 3 ]

โดยรูปแบบ Input มีดังนี้
1. append    ->  AP
2. addHead  ->  AH
3. search      ->  SE
4. index        ->   ID
5. size          ->   SI
6. pop          ->   PO
7. insert       ->   IS

โดยให้เพิ่มเติมจากส่วน #Code Here ของโปรแกรมต่อไปนี้ เพื่อให้สามารถแสดงผลได้ตามที่โจทย์กำหนด
********  ห้ามใช้ List ในการทำ Linked List เด็ดขาดถ้าหากพบจะถูกลดเป็น 0 คะแนน ******** '''

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

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
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
        if self.size() > pos and pos>0 :
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
        elif pos >= self.size():
            self.append(item)
        elif pos == 0 or -pos > self.size():
            self.addHead(item)
        else :
            now = self.tail
            index =- 1
            while now != None :
                if index != pos:
                    now = now.previous
                    index -= 1
                else :
                    newNode.previous = now.previous
                    newNode.next = now
                    now.previous.next = newNode
                    now.previous =newNode
                    now = now.previous
                    index -= 1

    def search(self, item):
        if self.index(item) != -1 :
            return "Found"
        else :
            return "Not Found"

    def index(self, item):
        now = self.head
        index = 0
        while now != None:
            if now.value == item:
                return index
            else :
                index += 1
            now = now.next
        return -1

    def size(self):
        size = 0
        now =self.head
        while now != None:
            size += 1
            now = now.next
        return size

    def pop(self, pos):
        index = 0
        now = self.head
        if self.size() != 0:
            if self.size()-1 > pos and pos > 0:
                while now != None :
                    if pos ==index:
                        now.previous.next = now.next
                        now.next.previous = now.previous
                    index +=1
                    now = now.next
            elif pos ==0 and self.size()==1:
                self.head = None
                self.tail = None
            elif pos ==0 :
                now.next.previous = None
                self.head = now.next
            elif pos == self.size()-1:
                now = self.tail
                now.previous.next = None
                self.tail = now.previous
            else :
                return "Out of Range"
            return "Success"
        else :
            return "Out of Range"


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())