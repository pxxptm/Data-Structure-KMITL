input = [ int(x) for x in input("Enter Input : ").split() ]

for i in range(len(input)-1) :

    isSwapped = False
    temp = [None]

    for j in range(len(input)-i-1) :

        if input[j] > input[j+1] :

            if input[j] not in temp :
                temp.pop()
                temp.append(input[j])

            input[j] , input[j+1] = input[j+1] , input[j]
            isSwapped = True

    if not isSwapped or i == len(input) - 2 :
        print("last step : ",input," move",temp,sep="")
        break
    else :
        print(i+1," step : ",input," move",temp,sep="")