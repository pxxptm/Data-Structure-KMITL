''' ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

หา Factorial ของ input ที่รับมา โดยใช้ Recursive '''

def factorial(n) :
    if n == 0 :
        return 1
    else :
        return n*factorial(n-1)

n = int(input("Enter Number : "))
print(n,"! = ",factorial(n),sep="")