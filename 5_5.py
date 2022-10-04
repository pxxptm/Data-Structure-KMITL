''' ให้น้องๆใช้ Linked List (เขียนเป็น class)  ในการทำ Radix Sort  (มีอยู่ในสไลด์เรียน 2 หน้าสุดท้าย)  ในรูปแบบน้อยไปมาก

โดยผลลัพธ์การทำ Radix Sort แสดงผลในแต่ละรอบว่าได้ผลลัพธ์เป็นอย่างไร  3 บรรทัดสุดท้ายจะเป็น ( จำนวนรอบ , Data ก่อนทำ Radix Sort และ Data หลังทำ Radix Sort )

การเรียงเลขจำนวนลบ จะเรียงตรงข้ามกับเลขจำนวนบวก จึงควรแยก การเรียงตัวเลขบวก และเลขลบ ออกจากกัน '''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.linkedListSize = 0

    def __str__(self):
        cur, s = self.head, str(self.head.value)
        while cur.next != None:
            s += " -> " + str(cur.next.value)
            cur = cur.next
        return s

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
        self.linkedListSize += 1


input = input("Enter Input : ").split()

before = " -> ".join(input)
 
Positive = LinkedList()
Negative = LinkedList()

maxVal = 0
minVal = 0
roundP = 0
roundN = 0

for element in input :
    if int(element) > maxVal and int(element) >= 0 :
        maxVal = int(element)
        roundP = len(element)
    elif int(element) < minVal and int(element) < 0 :
        minVal = int(element)
        roundN = len(element)-1

    if int(element) >= 0 :
        Positive.append(element)
    else :
        Negative.append(element[1:])

listP = [LinkedList() for e in range(roundP+1)]
listN = [LinkedList() for e in range(roundN+1)]

# sort positive number

digit = -1

for index in range(roundP+1) :
    if index == 0 :
        for i in range(10) :
            now = Positive.head
            while now :
                if i == int(str(now.value)[digit]) :
                    listP[index].append(now.value)
                now = now.next
    else :
        for i in range(10) :
            now = listP[index-1].head
            while now :
                if i == 0 and len(str(now.value)) < -digit :
                    listP[index].append(now.value)
                elif len(str(now.value)) >= -digit and i == int(str(now.value)[digit]) :
                    listP[index].append(now.value)
                now=now.next
    digit -= 1
    #print(index,":",listP[index])

# sort negative number

digit = -1

for index in range(roundN+1) :
    if index == 0 :
        for i in range(10) :
            now = Negative.head
            while now :
                if 9-i == int(str(now.value)[digit]) :
                    listN[index].append(now.value)
                now = now.next
    else :
        for i in range(10) :
            now = listN[index-1].head
            while now :
                if 9-i == 0 and len(str(now.value)) < -digit :
                    listN[index].append(now.value)
                elif len(str(now.value)) >= -digit and 9-i == int(str(now.value)[digit]) :
                    listN[index].append(now.value)
                now=now.next
    digit -= 1
    #print(index,":",listN[index])

ans = LinkedList()

nowP = listP[-1].head
nowN = listN[-1].head

while nowP :
    if not nowN is None :
        ans.append(int("-" + str(nowN.value)))
        nowN = nowN.next
    else :
        ans.append(int(nowP.value))
        nowP =nowP.next

after = str(ans)

print("------------------------------------------------------------")

round = int(1)
devider = 1

indexZero = LinkedList()

while True :
    print("Round : " + str(round))
    for i in range(10) :
        now = ans.head
        print(i,": ",end="")
        while now :
            if (now.value//devider)%10 == i and now.value >= 0 :
                print(now.value,end=" ")
                if i == 0 :
                    indexZero.append(now.value)
            elif (-now.value//devider)%10 == i and now.value < 0 :
                print(now.value,end=" ")
                if i == 0 :
                    indexZero.append(now.value)
            now = now.next
        print()

    print("------------------------------------------------------------")
    
    if indexZero.linkedListSize == ans.linkedListSize :
        break

    round += 1   
    devider *= 10
    indexZero = LinkedList()

print(round-1,"Time(s)")          
print("Before Radix Sort :",before)
print("After  Radix Sort :",after)