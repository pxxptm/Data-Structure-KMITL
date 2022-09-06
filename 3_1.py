'''   
    รู้จักกับ STACK

    ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา



    A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK

    P           ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น  -1

    *** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty  '''


class Stack :
    
    def __init__ (self , list = None) :
        if list == None :
            self.items = []
        else :
            self.items = list
    
    def push (self,i) :
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()
        
    def isEmpty(self):
        return self.items == []
        
    def size(self) :
        return len(self.items)
        
    def __str__(self):
        s = "Value in Stack ="

        if UserInput.isEmpty() :
            s += " Empty"
        else :
            for element in self.items :
                s += " " + str(element)

        return s
  
  
UserInput = Stack()

Input = input("Enter Input : ").split(",")

for element in Input :
    if element == "P" :
        if UserInput.isEmpty() :
            print("-1")
        else :
            print("Pop =",UserInput.pop(),"and Index =",UserInput.size())
    else :
        temp = element.split(" ")
        UserInput.push(temp[1])
        print("Add =",temp[1],"and Size =",UserInput.size())

print(UserInput)