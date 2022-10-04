''' ให้นักศึกษาเขียนฟังก์ชันที่ทำงานเหมือนกับฟังก์ชัน len() เพื่อหาความยาวของ string และแสดงผลดังตัวอย่าง(print ตัวอักษรตามด้วยเครื่องหมายพิเศษสลับกันคู่คี่)

****ห้ามใช้คำสั่ง len, for, while, do while, split*****

หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว

def length(txt):     
    #Code Here
print("\n",length(input("Enter Input : ")),sep="")
#ตรง print(เป็นแค่ตัวอย่างสามารถแก้ไขได้) '''

def length(txt) :     
    if txt is "" :
        return 0
    else :
        return 1 + length(txt[1:])

def specialCharAdd_Odd(txt) :
    if not txt :
        return ""
    else :
        if length(txt) % 2 == 1 :
                return txt[0] + "*" + specialCharAdd_Odd(txt[1:])
        else :
            return txt[0] + "~" + specialCharAdd_Odd(txt[1:])

def specialCharAdd_Even(txt) :
    if not txt :
        return ""
    else :
        if length(txt) % 2 == 0 :
                return txt[0] + "*" + specialCharAdd_Even(txt[1:])
        else :
            return txt[0] + "~" + specialCharAdd_Even(txt[1:])
        

txt = input("Enter Input : ")
l = length(txt)
if l % 2 == 0 :
    print(specialCharAdd_Even(txt),"\n",l,sep="")
else :
    print(specialCharAdd_Odd(txt),"\n",l,sep="")