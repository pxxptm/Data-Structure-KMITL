print("*** TorKham HanSaa ***")
input = input("Enter Input : ").split(",")

now = []
previous = ""

for element in input :

    if element == "X" :
        break
    elif element == "R" :
        now.clear()
        previous = ""
        print("game restarted")
    else :
        temp = element.split(" ")
        if temp[0] == "P" :

            cmp1 = temp[1][:2].lower()
            cmp2 = previous[-2:].lower()

            if ( cmp1 == cmp2 and previous != "" ):
                now.append(temp[1])
                previous = temp[1]
                print("\'" + temp[1] + "\'" + " -> ",end="")
                print(now)
            elif ( cmp1 != cmp2 and previous == "") :
                now.append(temp[1])
                previous = temp[1]
                print("\'" + temp[1] + "\'" + " -> ",end="")
                print(now)
            else :
                print("\'" + temp[1] + "\'" + " -> game over")
                break
            
        else :
            print("\'" + element + "\'" + " is Invalid Input !!!")
            break
            
