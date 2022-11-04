print("*** Fun with Drawing ***")

n = int(input("Enter input : "))

for i in range(2*n-1) :
    for j in range(4*n-3) :

        if i == 0 :
            print("#",end='')
        elif(i%2==1) :
            if j < i or j > 4*n-4-i :
                if j%2 == 1 :
                   print(".",end='')
                else :
                    print("#",end='') 
            else :
                print(".",end='')
        else :
            if j < i or j > 4*n-4-i :
                if j%2 == 1 :
                   print(".",end='')
                else :
                    print("#",end='') 
            elif j >= i and j <= 4*n-4-i :
                print("#",end='')
            else :
                print(".",end='')
        
    print()

i=0
j=0

for i in range(2*n-2) :

    for j in range(4*n-3) :

        if i == 2*n-3 :
            print("#",end='')
        elif(i%2==0) :
            if j < 2*n-2-i or j > 2*n-1+i :
                if j%2 == 1 :
                   print(".",end='')
                else :
                    print("#",end='') 
            else :
                print(".",end='')
        else :
            if j < 2*n-3-i or j > 2*n-1+i :
                if j%2 == 0 :
                   print("#",end='')
                else :
                    print(".",end='') 
            elif j >= i and j <= 2*n-1+i :
                print("#",end='')
            else :
                print("#",end='')
        
    print()