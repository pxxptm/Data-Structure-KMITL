'''
สมมติว่านักศึกษาแอบชอบคนๆหนึ่งอยู่ โดยที่นักศึกษาและคนๆนั้นจะมีกิจกรรมและสถานที่ที่ไปแตกต่างกันในแต่ละวัน
ให้นักศึกษาเขียนโปรแกรมที่จะหาว่าสิ่งที่นักศึกษาและคนๆนั้นทำในแต่ละวันจะทำให้ได้คบกันหรือไม่ โดยใช้ Queue

กิจกรรม                                       สถานที่
0 = กินข้าว(Eat)                           0 = ร้านอาหาร(Res.)
1 = เล่นเกม(Game)                      1 = ห้องเรียน(ClassR.)
2 = ทำโจทย์ datastruc(Learn)      2 = ห้างสรรพสินค้า(SuperM.)
3 = ดูหนัง(Movie)                        3 = บ้าน(Home)

โดยการรับ Input จะประกอบด้วย

กิจกรรม:สถานที่(ของนักศึกษาและของคนๆนั้น) โดยในแต่ละวันจะคั่นด้วยเครื่องหมาย ,

เช่น วันที่ 1 นักศึกษาไปกินข้าวที่ร้านอาหาร และ คนๆนั้นไปนั่งทำโจทย์ datastruc ที่ร้านอาหาร 
       วันที่ 2 นักศึกษาไปเล่นเกมที่บ้าน และ คนๆนั้นไปดูหนังที่ห้างสรรพสินค้า
จะได้ว่า 0:0 2:0,1:3 3:2

***มีการคิดคะแนนดังนี้***

·       กิจกรรมเดียวกันแต่คนละสถานที่         +1

·       สถานที่เดียวกันแต่ทำกิจกรรมต่างกัน    +2

·       กิจกรรมเดียวกันและสถานที่เดียวกัน    +4

·       ไม่เหมือนกันเลย                                   - 5

หากมีคะแนนมากกว่าหรือเท่ากับ 7 จะถือว่าได้คบกัน แต่ถ้าคะแนนน้อยกว่า 7 แต่มากกว่า 0 เป็นคนคุย น้อยกว่านั้นถือว่าเป็นได้แค่เพื่อน

โดยในแต่ละขั้นตอนให้แสดงผลดังตัวอย่าง
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
        for i in range(0,self.size()) :
            s += str(self.items[i])
            if i == self.size()-1 :
                continue
            else :
                s += ", "

        return s

activity = [ "Eat" , "Game" , "Learn" , "Movie" ]
location = [ "Res." , "ClassR." , "SuperM." , "Home" ]

my = Queue()
your = Queue()

pt = 0

input = input("Enter Input : ").split(",")

for element in input :
    pair = element.split()

    my.enQueue(pair[0])
    your.enQueue(pair[1])

    if pair[0] == pair[1] :
        pt += 4
    else :
        i = pair[0].split(":")
        u = pair[1].split(":")

        #print(i , " " , u)

        if i[0] == u[0] :
            pt += 1
        elif i[-1] == u[-1] :
            pt += 2
        else :
            pt -= 5

    #print(pair[0], " " ,pair[1]," " ,pt)

print("My   Queue =",my)
print("Your Queue =",your)

print("My   Activity:Location = ",end="")

count = 0

for element in my.returnQueue() :
    temp = element.split(":")
    s = activity[int(temp[0])] + ":" + location[int(temp[1])]
    print(s,end="")
    count += 1
    if count < my.size() :
        print(", ",end="")

print("\nYour Activity:Location = ",end="")

count = 0

for element in your.returnQueue() :
    temp = element.split(":")
    s = activity[int(temp[0])] + ":" + location[int(temp[1])]
    print(s,end="")
    count += 1
    if count < your.size() :
        print(", ",end="")

if pt >= 7 :
    print("\nYes! You're my love! : Score is ",pt,".",sep="")
elif pt > 0 : 
    print("\nUmm.. It's complicated relationship! : Score is ",pt,".",sep="")
else :
    print("\nNo! We're just friends. : Score is ",pt,".",sep="")