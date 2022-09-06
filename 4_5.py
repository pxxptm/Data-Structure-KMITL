'''
เกม Color Crush 2

คืออะไร : Color Crush จะเป็นเกมที่นำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  ABBBA  -> AA  เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  ถ้าหากมีการเรียงกันแบบ  ABBBAA -> Empty  เนื่องจาก  ถ้าหาก B ระเบิด  A(BBB)AA -> AAA จะเห็นว่า A ก็เรียงกันอีก 3 ตัวทำให้เกิดการระเบิดขึ้นอีกครั้งหนึ่ง  และถ้าหากมีการเรียงกันแบบ AAAA -> A เนื่องจากมีการเรียงกัน 3 ตัว  (AAA)A ทำให้เหลือ A 1 ตัว

เนื้อเรื่อง :  หลังจากที่กฤษฎาได้เล่นเกม Color Crush ก็ได้ไปเห็นโฆษณาว่า บริษัทที่ได้สร้าง Color Crush มีแผนการที่จะสร้างเกม Color Crush 2 ขึ้นมา กฤษฎาจึงได้สมัครเข้าไปร่วมทีมในการสร้างเกม Color Crush 2 ซึ่งเกมนี้จะมีกิมมิคที่แตกต่างออกไป คือการที่จะมี 2 ฝั่ง คือ ฝั่งปกติกับฝั่งโลกกระจก โดยฝั่งโลกกระจกจะเกิดการระเบิดก่อน ซึ่งการระเบิดของฝั่งโลกกระจกจะไม่ใช่ระเบิดแล้วหายไปเลย แต่จะเป็นระเบิดแล้วกลายเป็น ITEM ไว้สำหรับขัดขวางการระเบิดของฝั่งปกติ  หลังจากที่ฝั่งโลกกระจกเกิดการระเบิดครบแล้ว ก็จะเป็นคิวของฝั่งปกติ  ซึ่งถ้าหากฝั่งปกติมีการเรียงกันของสีที่จะทำให้เกิดการระเบิด ในเสี้ยววินาทีนั้นก่อนที่จะเกิดการระเบิดของฝั่งปกติ  ITEM สำหรับขัดขวางการระเบิดของฝั่งโลกกระจก จะมาคั่นระหว่างระเบิดลูกที่ 2 กับ ลูกที่ 3 (อาจจะทำให้เกิดการระเบิดเหมือนเดิมได้ถ้าหาก ระเบิดนั้นเป็นสีเดียวกัน  แต่ถ้าเป็นคนละสีก็จะทำให้ไม่เกิดการระเบิดขึ้น)  โดยระเบิดอาจจะเกิดการระเบิดซ้อนๆกันเรื่อยๆได้จะเป็น Empty  เช่น ถ้าหากฝั่งปกติมีระเบิดเรียงแบบนี้ AAAAA และฝั่งโลกกระจกมีระเบิดแบบนี้ AAA ถ้าหากฝั่งปกติระเบิดธรรมดา 1 ทีจะเหลือแค่ AA แต่ถ้าหากฝั่งโลกกระจกมาขัดขวาง จะกลายเป็น AA(A)AAAA ก็จะเกิดระเบิด 2 ทีทำให้ระเบิดฝั่งปกติเป็น Empty

อธิบายรูปแบบ Input ของ Test_Case_1 : ฝั่งปกติจะมีระเบิดเรียงดังนี้ -> AAABBBCDEE  ฝั่งโลกกระจกจะมีระเบิดเรียงดังนี้ -> HHH โดยฝั่งโลกกระจกจะมีระเบิด H ที่เป็น ITEM สำหรับขัดขวาง 1 ลูกไว้สำหรับขัดขวางการระเบิดที่จะเกิดขึ้นกับฝั่งปกติได้  ต่อมาฝั่งปกติจะเกิดการระเบิดของ A และ B ตามลำดับ  โดยฝั่งโลกกระจกจะนำระเบิด H ไปขัดขวางการระเบิดของระเบิด A เพราะระเบิด A เกิดการระเบิดก่อนระเบิด B  โดยการขัดระเบิดนั้นจะเป็นการขัดระหว่างลูกที่ 2 กับลูกที่ 3 เพื่อให้เห็นภาพ -> AAABBBCDEE -> AA(H)ABBBCDEE  -> AA(H)ACDEE ลำดับจะเป็นดังนี้  และฝั่งปกติเกิดการระเบิด 1 ครั้ง ส่วนฝั่งโลกกระจกก็เกิดการระเบิดอีก 1 ครั้ง

อธิบายรูปแบบ Input ของ Test_Case_3 : ฝั่งปกติจะมีระเบิดเรียงดังนี้ -> AAABBBCDDDEE  ฝั่งโลกกระจกจะมีระเบิดเรียงดังนี้ -> BBBTENETAAA โดยฝั่งโลกกระจกจะมีระเบิด A และ B ที่เป็น ITEM สำหรับขัดขวาง 2 ลูกตามลำดับไว้สำหรับป้องกันการระเบิดที่จะเกิดขึ้นกับฝั่งปกติได้  ต่อมาฝั่งปกติจะเกิดการระเบิดของ A B และ D ตามลำดับ  โดยฝั่งโลกกระจกจะนำระเบิด A  ไปขัดขวางการระเบิดของระเบิด A เพราะระเบิด A เกิดการระเบิดก่อนระเบิด B  โดยการขัดระเบิดนั้นจะเป็นการขัดระหว่างลูกที่ 2 กับลูกที่ 3  เพื่อให้เห็นภาพ -> AAABBBCDDDEE -> AA(A)ABBBCDDDEE -> ABBBCDDDEE ลำดับจะเป็นดังนี้  ต่อมาจะนำระเบิด B ไปขัดขวางการระเบิดของระเบิด B เพื่อให้เห็นภาพ  ABBBCDDDEE -> ABB(B)BCDDDEE -> ABCDDDEE  ต่อมาเกิดการระเบิดอีก 1 ครั้ง ABCDDDEE -> ABCEE ซึ่งฝั่งโลกกระจกไม่สามารถขัดขวางได้เพราะ ITEM สำหรับขัดขวางหมดแล้ว   และฝั่งปกติเกิดการระเบิดทั้งหมด 3 ครั้ง  ซึ่ง 2 ครั้งเกิดจากการที่ฝั่งโลกกระจกใส่ระเบิดสีเดียวกันมาซึ่งถือว่าเป็นการขัดขวางที่ผิดหและเกิดการระเบิดเองอีก 1 ครั้ง ส่วนฝั่งโลกกระจกก็เกิดการระเบิดอีก 2 ครั้ง

อธิบายรูปแบบ Output : แบ่งออกเป็น 2 ฝั่งคือฝั่งปกติกับฝั่งโลกกระจก  โดยบรรทัดแรกจะเป็นจำนวนระเบิดที่เหลืออยู่ บรรทัดที่สองจะเป็นระเบิดที่เหลืออยู่แต่ถ้าหากไม่มีระเบิดเหลืออยุ่เลยให้แสดง "Empty" บรรทัดที่สามจะเป็นจำนวนที่เกิดระเบิดขึ้น บรรทัดที่สี่จะมีเฉพาะฝั่งปกติถ้าหากเกิดเหตุการณ์ที่ ITEM ของฝั่งโลกกระจกมาขัดขวาง แต่ระเบิดนั้นดันเป็นลูกเดียวกับที่จะเกิดการระเบิด  ส่วนทีมสีน้ำเงินจะเหมือนกับทีมสีแดงแต่บรรทัดที่ 2 กับ 3 และชื่อทีม จะเป็นแบบ inverse

คำใบ้ - ใช้ Stack ในการหาลูกระเบิดเรียงกัน 3 ลูก   โดยให้ทำฝั่งโลกกระจกก่อนว่ามีระเบิดลูกอะไรบ้าง (ก่อนเข้า stack ให้ Reverse ก่อน)  จากนั้นเก็บลง Queue แล้วไปทำฝั่งปกติถ้าหากฝั่งปกติเกิดการระเบิดก็ DeQueue ระเบิดที่ได้รับมาจากฝั่งกระจกมาขัดระเบิดระหว่างลูกที่ 2 กับ 3

อธิบาย Case 10:

ฝั่งซ้าย = DDDFFFGGG
ฝั่งขวา = ABBBAACCC
ทำฝั่งขวาก่อนโดยการ inverse ABBBAACCC -> CCCAABBBA จะได้ระเบิดมา 3 ลูกคือ C B A ตามลำดับจากนั้นเก็บลง Queue ต่อมาดูที่ฝั่งซ้าย DDD จะเกิดการระเบิดเราจะนำ C ไปขัด | ต่อมา F จะระเบิดเราจะนำ B มาขัด | ต่อมา G จะระเบิดเราจะนำ A มาขัด   สุดท้ายจะกลายเป็น DDCDFFBFGGAG
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

        for character in self.items :
            s+=character

        return s

def PopMirror(list) :
    item = Queue()

    l = list
    l.reverse()
    
    index = 1
    explored = 0

    while index < len(l)-1 :
        if l[index] == l[index-1] == l[index+1] :
            item.enQueue(l[index])
            l.pop(index-1)
            l.pop(index-1)
            l.pop(index-1)
            index = 1
            explored += 1
        else :
            index += 1
        
    return l,item,explored

def PopNormal(list,interupt) :
    
    l = list
    failed = 0
    explored_by_item = 0
    explored = 0

    # insert interrupt & count failed

    index = 1

    while index < len(l)-1 :
        if l[index] == l[index-1] == l[index+1] :
            if interupt.size() > 0 :
                item = interupt.deQueue()
                l.insert(index+1,item)
                if item == l[index] :
                    failed += 1
                    explored_by_item += 1

            index += 2
        else :
            index += 1

    
    index = 1

    while index < len(l)-1 :
        if l[index] == l[index-1] == l[index+1] :
            l.pop(index-1)
            l.pop(index-1)
            l.pop(index-1)
            index = 1
            explored += 1
        else :
            index += 1
        
    return l,explored-explored_by_item,failed
    

def showCharInList(list) :
    s = ""
    for character in list :
        s += str(character)

    return s

Normal = []
Mirror = []
Item = []

normal,mirror = input("Enter Input (Normal, Mirror) : ").split()

# Normal
for color in normal :
    Normal.append(color)

# Mirror
for color in mirror :
    Mirror.append(color)

Mirror , Item , exploredM = PopMirror(Mirror)
Normal , exploredN , failed = PopNormal(Normal,Item)

print("NORMAL :")
print(len(Normal))

if len(Normal) > 0 :
    print((showCharInList(Normal))[::-1])
else :
    print("Empty")

print(exploredN,"Explosive(s) ! ! ! (NORMAL)")

if failed > 0 :
    print("Failed Interrupted",failed,"Bomb(s)")

print("------------MIRROR------------\n: RORRIM")
print(len(Mirror))

if len(Mirror) > 0 :
    print(showCharInList(Mirror)[::-1])
else :
    print("ytpmE")

print("(RORRIM) ! ! ! (s)evisolpxE",exploredM)
