''' ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive รับค่า a,b โดยที่ a,b เป็นจำนวนเต็มบวกหรือศูนย์ และค่าหา ab  '''

def recursivePow(a,b) :
    if b == 0 :
        return a
    else :
        return a * pow(a,b-1)

a,b = input("Enter Input a b : ").split()
a = int(a)
b = int(b)
print(pow(a,b))