'''
    ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ Queue ในการแก้ปัญหา

    E  <value>  ให้นำ value ไปใส่ใน Queue และทำการแสดงผล ข้อมูลปัจจุบันของ Queue

    D           ให้ทำการ Dequeue ตัวที่อยู่หน้าสุดของ Queue ออก หลังจากนั้นแสดงตัวเลขที่เอาออกมา และ แสดงผลข้อมูลปัจจุบันของ Queue

    ***และเมื่อจบการทำงานให้แสดงผลข้อมูลปัจจุบันของ Queue พร้อมกับข้อมูลที่ถูก Dequeue ทั้งหมดตามลำดับ
    ***ถ้าหากไม่มีข้อมูลใน Queue แล้วให้แสดงคำว่า  Empty
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
        s = ""

        if self.isEmpty() :
            s = "Empty"
        else :
            for i in range(0,self.size()) :
                s += str(self.items[i])
                if i == self.size()-1 :
                    continue
                else :
                    s += ", "

        return s


q = Queue()
deQ = Queue()

UserInput = input("Enter Input : ").split(",")

while len(UserInput) > 0 :
    temp = UserInput.pop(0).split()

    if temp[0] == "E" :
        q.enQueue(temp[1])
        print(q)
    else :
        if q.isEmpty() :
            print("Empty")
        else :
            deq = q.deQueue()
            deQ.enQueue(deq)
            print(deq,"<-",end=" ")

            if q.isEmpty() :
                print("Empty")
            else :
                print(q)

print(deQ,":",q)