'''
    จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้

    A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack

    P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )

    D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  

    LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

    MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

    การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม

    *** Hint ***

    ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ
'''

class Stack :
    
    def __init__ (self , list = None) :
        if list == None :
            self.items = []
        else :
            self.items = list
    
    def add (self,i) :
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()

    def peek(self) :
        return self.items[-1]
        
    def isEmpty(self):
        return self.items == []
        
    def size(self) :
        return len(self.items)
        
    def __str__(self) :
        s = "Value in Stack = [" 

        for i in range(0,self.size()) :
            s += self.items[i]
            if i == self.size()-1 :
                continue
            else :
                s += ", "

        s += "]"
        return s


# ManageStack Function

def ManageStack(list) :

    UserInput = Stack()
    copy = Stack()
    Input = list.split(",")

    for element in Input :
        if element == "P" :
            if UserInput.isEmpty() :
                print("-1")
            else :
                print("Pop =",UserInput.pop())

        else :
            temp = element.split(" ")
                
            if temp[0] == "A" :
                UserInput.add(temp[1])
                print("Add =",temp[1])

            elif temp[0] == "D" :
                if UserInput.isEmpty() :
                        print("-1")
                else :
                    while not UserInput.isEmpty() :
                        if int(UserInput.peek()) == int(temp[1]) :
                            print('Delete =',UserInput.peek())
                            UserInput.pop()
                        else :
                            copy.add(UserInput.peek())
                            UserInput.pop()
                
                while not copy.isEmpty():
                    UserInput.add(copy.peek())
                    copy.pop()

            elif temp[0] == "LD" :
                if UserInput.isEmpty() :
                    print("-1")
                else :
                    while not UserInput.isEmpty() :
                        if int(UserInput.peek()) < int(temp[1]) :
                            print('Delete =',UserInput.peek(),"Because",UserInput.peek(),"is less than",int(temp[1]))
                            UserInput.pop()
                        else :
                            copy.add(UserInput.peek())
                            UserInput.pop()
                
                while not copy.isEmpty():
                    UserInput.add(copy.peek())
                    copy.pop()


            elif temp[0] == "MD" :
                if UserInput.isEmpty() :
                    print("-1")
                else :
                    while not UserInput.isEmpty() :
                        if int(UserInput.peek()) > int(temp[1]) :
                            print('Delete =',UserInput.peek(),"Because",UserInput.peek(),"is more than",int(temp[1]))
                            UserInput.pop()
                        else :
                            copy.add(UserInput.peek())
                            UserInput.pop()
                
                while not copy.isEmpty():
                    UserInput.add(copy.peek())
                    copy.pop()
    return UserInput
                        
Input = input("Enter Input : ")
print(ManageStack(Input))