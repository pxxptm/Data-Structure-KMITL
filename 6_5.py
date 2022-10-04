''' เขียนโปรแกรมที่แสดงผลดังตัวอย่าง

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

def staircase(n):
    #code here

print(staircase(int(input("Enter Input : ")))) '''

def staircasePos(n,step):
    if step <= n :
        print("_"*(n-step),"#"*step,sep="")
        staircasePos(n,step+1)

def staircaseNeg(n,step):
    if step > 0 :
        print("_"*(n-step),"#"*step,sep="")
        staircaseNeg(n,step-1)

n = int(input("Enter Input : "))

if n == 0 :
    print("Not Draw!")
elif n > 0 :
    staircasePos(n,1)
else :
    n = abs(n)
    staircaseNeg(n,n)