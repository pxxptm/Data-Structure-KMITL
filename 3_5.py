'''
ที่จอดรถของนาย ก เป็นส่วนที่แรเงาสีฟ้า ส่วนสีแดงเป็นที่ของนาย ข ซี่งเป็นญาติกัน ที่จอดรถของนาย ก และ นาย ข แคบมาก จอดรถได้เรียงเดี่ยว นาย ข ไม่ได้ใช้ที่จอดรถ แต่ อนุญาติให้นาย ก ใช้ที่จอดรถของเขาได้โดยไม่จอดรถแช่ไว้ เนื่องจากซอยแคบ ดังนั้นการมาจอด (arrive) และการรับรถ (depart)จะเป็นลักษณะของ stack เงื่อนไขคือ ในการรับรถ x ใดๆอยากให้ลำดับรถเป็นเหมือนเดิม ดังรูป simulate การจอดรถในที่จอดรถของนาย ก โดยใช้ operation ของ stack ข้างล่างเป็นตัวอย่าง output

การรับ input : รับ input 4 ค่าใน 1 บรรทัดโดยให้แยกโดย " " (space bar) โดยตำแหน่งแรกคือ จำนวนสูงสุดที่รถสามารถจอดได้ในซอยของ นาย ก ตำแหน่งที่สองคือ รถที่จอดอยู่ในซอยของ นาย ก ตำแหน่งที่สามคือ การกระทำเช่น ถ้าเป็น arrive จะทำการเพิ่มรถในซอย ส่วน depart จะทำการเอารถออกจากซอย โดยรถที่จะทำการเพิ่มหรือนำออกนั้นจะเป็น เลขในตำแหน่งที่ 4

***หมายเหตุ ถ้าในซอยไม่มีรถอยู่เลยให้ input = 0 ในตำแหน่งที่ 2***
'''
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

    def peek(self) :
        return self.items[-1]
        
    def isEmpty(self):
        return self.items == []
        
    def size(self) :
        return len(self.items)
        
    def __str__(self) :
        s = "[" 

        for i in range(0,self.size()) :
            s += str(self.items[i])
            if i == self.size()-1 :
                continue
            else :
                s += ", "

        s += "]"
        return s



print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()

m,n = int(m),int(n)
s = s.split(",")

stack = Stack()

if s == ["0"] :
    pass
else :
    for i in range (0,len(s)) :
        stack.push(s[i])

#print(stack)

if o == "arrive" :
    if str(n) in s :
        print("car",n,"already in soi")
    elif stack.size() < m :
        stack.push(n)
        print("car",n,"arrive! : Add Car",n)
    else :
        print("car",n,"cannot arrive : Soi Full")
else :
    if stack.isEmpty() :
        print("car",n,"cannot depart : Soi Empty")
    elif not str(n) in s :
        print("car",n,"cannot depart : Dont Have Car",n)
    else :
        temp = Stack()

        while not stack.isEmpty() :
            if int(stack.peek()) != n :
                temp.push(stack.peek())
            stack.pop()
                
        while not temp.isEmpty():
            stack.push(temp.peek())
            temp.pop()

        print("car",n,"depart ! : Car",n,"was remove")

print(stack)