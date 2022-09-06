'''
    จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

    โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

    แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ

    แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ

    ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2

    จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2] จนกว่าแถวหลักจะหมด
'''
class Queue:

    def __init__(self, list = None) :
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def returnQueue(self):
        return self.items

    def __str__(self) :
        return str(self.items)

mainQ = Queue()
q1 = Queue()
q2 = Queue()

tMain = 1
t1 = 0
t2 = 0

people = input("Enter people : ")

for i in range (0,len(people)) :
    mainQ.enQueue(people[i])

while not mainQ.isEmpty() :

    if not q1.isEmpty() :
        if t1 % 3 == 0 :
            q1.deQueue()


    if not q2.isEmpty() :
        if t2 % 2 == 0 :
            q2.deQueue()


    if q1.size() < 5 :
        q1.enQueue(mainQ.deQueue())
    elif q2.size() < 5 :
        q2.enQueue(mainQ.deQueue())


    if not q1.isEmpty() :
        t1 += 1

    if not q2.isEmpty() :
        t2 += 1


    print(tMain,mainQ,q1,q2)
    tMain += 1
